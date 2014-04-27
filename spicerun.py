#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
_log = logging.getLogger(__name__)

import os, os.path, shutil

import subprocess

from simbench.util import rmrf

import spice2hdf

_dft_conf = {
    'gnetlist':'gnetlist',
    'gnetlist.cmd':"%(gnetlist)s -g spice-sdb -O include_mode -O nomunge_mode -o %%(net)s %%(sch)s",
    'spice':'ngspice',
    'spice.cmd':'%(spice)s --no-spiceinit --pipe %%(deck)s',
}


def getargs(args=None):
    from spice2hdf import h5group
    import argparse, sys
    
    P = argparse.ArgumentParser(description='Execute a simbench .sprj simulation')
    P.add_argument('infile', type=argparse.FileType('r'), metavar='input.sprj',
                   help="A .sproj file")
    P.add_argument('outfile', type=h5group(), metavar='out.h5[:/a/b]',
                   help="An HDF5 with optional H5 Group (/ if omitted)")
    P.add_argument('--verbose', '-v', action='store_const', default=logging.INFO, const=logging.DEBUG)
    P.add_argument('--quiet', '-q', action='store_const', dest='verbose', const=logging.WARN)
    P.add_argument('--config','-C', metavar='FILE', type=argparse.FileType('r'),
                   help='Use config file instead of default')

    return P.parse_args(args=args or sys.argv[1:])

def loadProject(FP):
    import json
    D = json.load(FP)
    if not isinstance(D, dict) or 'net' not in D or D.get('version',0)!=1:
        raise ValueError("Invalid file contents: %s"%FP.name)
    # expand paths to absolute
    D['projectdir'] = os.path.abspath(os.path.dirname(FP.name))
    D['net']['filename'] = os.path.join(D['projectdir'], D['net']['filename'])
    if _log.isEnabledFor(logging.DEBUG):
        _log.debug("D: %s", D)
    return D

def loadConfig(FP=None):
    from ConfigParser import SafeConfigParser as ConfigParser
    P = ConfigParser(defaults=_dft_conf)
    P.add_section('spicerun')
    P.read([
        '/etc/spicerun.conf',
        os.path.expanduser('~/.config/spicetools/spicerun.conf'),
        'spicerun.conf'
    ])
    if FP:
        P.readfp(FP)

    return dict([(K,P.get('spicerun',K)) for K in _dft_conf.iterkeys()])

def genNet(D, conf, outfile):
    netdir = os.path.dirname(D['net']['filename'])

    A = {
        'net':outfile,
        'sch':D['net']['filename'],
    }
    cmd = conf['gnetlist.cmd']%A
    _log.debug("In: %s",os.path.dirname(A['sch']))
    _log.debug("Running: '%s'", cmd)

    subprocess.check_call(cmd, shell=True, cwd=netdir)

def runSpice(D, conf, deck, outdir):
    A = {
        'deck':deck,
    }
    cmd = conf['spice.cmd']%A

    _log.debug("In: %s",outdir)
    _log.debug("Running: '%s'", cmd)

    subprocess.check_call(cmd, shell=True, cwd=outdir)

def writeDeck(D, FP, netfile, outdir):

    FP.write(_script_header%{
        'netfile':netfile,
        'netdir':os.path.dirname(D['net']['filename']),
        'workdir':outdir,
    })

    outfiles = []

    topvars = dict([(V['name'],V['expr']) for V in D.get('vars',[])])

    for S in D.get('sims',[]):
        FP.write(_script_sim%S)

        locvars = dict([(V.name,V.expr) for V in S.get('vars',[])])

        Vars = topvars.copy()
        Vars.update(locvars)

        for K,V in Vars.iteritems():
            FP.write('let %s = %s'%(K,V))

        FP.write('write %s.raw\n'%S['name'])
        outfiles.append(('%s.raw'%S['name'], S['name']))

    FP.write(_script_end)
    return outfiles

_script_header = """* %(netfile)s
.control
set filetype = binary
set sourcepath = ( %(netdir)s $sourcepath )
echo sourcepath = $sourcepath
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

class TempDir(object):
    def __init__(self, *args, **kws):
        self._args = (args, kws)
    def __enter__(self):
        args, kws = self._args
        import tempfile
        self.dirname = tempfile.mkdtemp(*args, **kws)
        _log.debug("Using temp dir: %s", self.dirname)
        return self.dirname
    def __exit__(self, A, B, C):
        rmrf(self.dirname)
        _log.debug("Removed temp dir: %s", self.dirname)

def main(args):
    D = loadProject(args.infile)
    conf = loadConfig(args.config)

    with TempDir() as outdir:
        _log.debug("Temp dir %s", outdir)
        netfile = os.path.join(outdir, 'generated.net')
        if D['net']['schem']:
            _log.info("Generate netlist")
            genNet(D, conf, netfile)
        else:
            shutil.copy(D['net']['filename'], netfile)
            netfile = D['net']['filename']

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

        _log.info("Aggregating output files")

        for raw,grp in rawfiles:
            A2 = spice2hdf.getargs([os.path.join(outdir,raw), '<<<skip>>>'])
            A2.outfile = args.outfile.require_group(grp)
            _log.info("Process %s", A2)
            spice2hdf.main(A2)

    _log.info("Done")

if __name__=='__main__':
    args = getargs()
    logging.basicConfig(format='%(asctime)s %(message)s',
                        level=args.verbose)
    main(args)
