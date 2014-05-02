#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
_log = logging.getLogger(__name__)

import os, os.path, shutil

import subprocess, re

from .util import TempDir
from .conf import loadConfig

from . import raw2hdf
from .run import UserError

def getargs(args=None):
    from .run import h5group, addCommonArgs
    import argparse
    
    P = argparse.ArgumentParser(description='Execute a simbench .sprj simulation')
    P.add_argument('infile', type=argparse.FileType('r'), metavar='input.sprj',
                   help="A .sproj file")
    P.add_argument('outfile', type=h5group(), metavar='out.h5[:/a/b]',
                   help="An HDF5 with optional H5 Group (/ if omitted)")
    P.add_argument('--config','-C', metavar='FILE', type=argparse.FileType('r'),
                   help='Use config file instead of default')
    addCommonArgs(P)

    return P

def loadProject(FP):
    import json
    D = json.load(FP)
    if not isinstance(D, dict) or 'net' not in D or D.get('version',0)!=1:
        raise ValueError("Invalid file contents: %s"%FP.name)
    # expand paths to absolute
    D['projectfile'] = os.path.abspath(FP.name)
    D['projectdir'] = os.path.dirname(D['projectfile'])
    D['net']['filename'] = os.path.join(D['projectdir'], D['net']['filename'])
    if _log.isEnabledFor(logging.DEBUG):
        _log.debug("D: %s", D)
    return D

_include = re.compile(r'(\s*\.include\s+)(\S+)(\s*)', re.IGNORECASE)

def expandInclude(F, OP, idir):
    """Read in a deck and recursively expand .include cards
    """
    # list of currently opened file names
    stacknames = [os.path.abspath(F)]
    # set of all names visited (not good to include the same file twice...)
    visited = set(stacknames)
    stack = [open(stacknames[0], 'r')]

    try:
        while len(stack):
            FP = stack[-1]
            L = FP.readline()

            if not L:
                FP.close()
                stack.pop()
                stacknames.pop()
                continue

            M = _include.match(L)
            if M is None:
                OP.write(L)
                continue
            _log.info("%s includes %s", FP.name, M.group(2))

            infile = os.path.join(idir, M.group(2))
            if infile in stacknames:
                _log.error("From: %s", FP.name)
                _log.error("Include path: %s", ' -> '.join(stacknames))
                raise ValueError("Recursive include of %s"%infile)
            elif infile in visited:
                continue

            stacknames.append(infile)
            visited.add(infile)
            stack.append(open(os.path.join(idir, M.group(2))))

    finally:
        [FP.close() for FP in stack]

def genNet(D, conf, outfile):
    netdir = os.path.dirname(D['net']['filename'])

    A = {
        'net':outfile,
        'sch':D['net']['filename'],
    }
    cmd = conf['gnetlist.cmd']%A
    _log.debug("In: %s",netdir)
    _log.debug("Running: '%s'", cmd)

    if subprocess.call(cmd, shell=True, cwd=netdir):
        raise UserError("gnetlist run failed\nIn: %s\nRunning %s"%(netdir, cmd))

def runSpice(D, conf, deck, outdir):
    A = {
        'deck':deck,
    }
    cmd = conf['spice.cmd']%A

    _log.debug("In: %s",outdir)
    _log.debug("Running: '%s'", cmd)

    if subprocess.call(cmd, shell=True, cwd=outdir):
        raise UserError("Spice run failed\nIn: %s\nRunning %s"%(outdir, cmd))

def writeDeck(D, FP, netfile, outdir):

    FP.write(_script_header%{
        'netfile':netfile,
        'netdir':os.path.dirname(D['net']['filename']),
        'workdir':outdir,
    })

    outfiles = []

    topvars = [(V['name'],V['expr']) for V in D.get('vars',[])]

    for S in D.get('sims',[]):
        FP.write(_script_sim%S)

        locvars = [(V['name'],V['expr']) for V in S.get('vars',[])]

        for K,V in topvars+locvars:
            FP.write('let %s = %s\n'%(K,V))

        if S['line'].strip()=='op':
            FP.write('print all\n')
        FP.write('write %s.raw\n'%S['name'])
        outfiles.append(('%s.raw'%S['name'], S['name']))

    FP.write(_script_end)
    return outfiles

_script_header = """* %(netfile)s
.control
set filetype = binary
echo "Loading Netlist"
shell ls -l
source generated.net
echo "Loaded Netlist"
"""

_script_sim = """echo "Analysis %(name)s"
%(line)s
"""

_script_end = """echo "Deck Done"
shell ls -l
quit
.endc
.end
"""

def main(args):
    D = loadProject(args.infile)
    conf = loadConfig(args.config, 'spicerun')

    with TempDir() as outdir:
        _log.debug("Temp dir %s", outdir)
        inpfile = os.path.join(outdir, 'input.net')
        netfile = os.path.join(outdir, 'generated.net')
        if D['net']['schem']:
            _log.info("Generate netlist")
            genNet(D, conf, inpfile)
        else:
            shutil.copy(D['net']['filename'], inpfile)

        # Expand .include cards

        with open(netfile, 'w') as FP:
            expandInclude(inpfile, FP, os.path.dirname(D['net']['filename']))

        if _log.isEnabledFor(logging.DEBUG):
            with open(netfile, 'r') as FP:
                _log.debug("Netlist: %s", FP.read())

        deck = os.path.join(outdir, 'generated.cmd')
        _log.info("Write spice deck: %s", deck)
        with open(deck, 'w+') as FP:
            rawfiles = writeDeck(D, FP, netfile, outdir)
            if _log.isEnabledFor(logging.DEBUG):
                FP.seek(0)
                _log.debug(FP.read())

        _log.info("Run spice")
        runSpice(D, conf, deck, outdir)

        _log.info("Aggregating output files to %s", args.outfile.file.filename)

        for raw,grp in rawfiles:
            A2 = raw2hdf.getargs()
            A2 = A2.parse_args([os.path.join(outdir,raw), '<<<skip>>>'])
            A2.outfile = args.outfile.require_group(grp)
            _log.info("Process %s", A2)
            raw2hdf.main(A2)

    _log.info("Done")

if __name__=='__main__':
    args = getargs().parse_args()
    logging.basicConfig(format=args.format,
                        level=args.level)
    main(args)
