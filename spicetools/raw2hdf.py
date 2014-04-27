# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
_L = logging.getLogger(__name__)

import numpy as np

from .run import h5group, addCommonArgs

_DESC="""Convert ngspice output files to a hdf5 format.

An example of storing 3 vector sets in one HDF5 file
for later plotting with spiceviewer
$ ngspice ...
 dc ...
 write dc1.raw
 dc ...
 write dc2.raw
 ac ...
 write ac1.raw
 quit
$ %(prog)s dc1.raw out.h5:/dc1
$ %(prog)s dc2.raw out.h5:/dc2
$ %(prog)s ac1.raw out.h5:/ac1
"""

def getargs():
    import argparse

    P = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    P.description = _DESC%{'prog':P.prog}
    P.add_argument('infile', type=argparse.FileType('r'), metavar='in.raw',
                   help="A spice ascii or binary output data file")
    P.add_argument('outfile', type=h5group(), metavar='out.h5[:/a/b]',
                   help="An HDF5 with optional H5 Group ('/' if omitted)")
    addCommonArgs(P)
    return P

def readHeader(inp):
    """Read the ascii header common to both binary and ascii formats

    Returns with the file pointer at the start of the data section
    """

    cont = False # continuation of previous line
    K = None # Current key
    header = {}
    N = 0
    while True:
        L = inp.readline()
        if not L:
            _L.error('Unexpected end of file after line %d', N)
            break
        N += 1
        if not L.strip():
            continue # skip blank lines (shouldn't be necessary)

        if cont and K=='variables':
            if L[0] not in '\t ':
                # end of Variables section
                cont = False
            else:
                parts = L.split(None, 2)
                if len(parts)!=3:
                    raise ValueError('Invalid variable on line %d'%N)
                idx, name, vtype = parts
                vars = header[K]
                assert int(idx)==len(vars), "Variable definition out of order on line %d"%N
                vars.append((name, vtype[:-1]))
                continue

        if not cont:
            assert L[0] not in '\t ', 'Line %d: expected assignment, found leading space'%N
            K, _, val = L.partition(':')
            K, val = K.lower(), val.strip()

            if K=='variables':
                cont = True
                header[K]=[]
                continue

            if K in ['no. variables','no. points']:
                val = int(val)
            elif K in ['values','binary']:
                # start of data section
                header[K]=None
                break

            if K in header:
                _L.warn('Duplicate header "%s"', K)
            header[K] = val

        else:
            assert False, "Formating error on line %d"%N

    if header.get('flags') not in ['real','complex']:
        raise ValueError('Unknown flags in header "%s"'%header['flags'])
    return header

_flags = {
    'real':np.float64,
    'complex':np.complex128,
}

def createOutputSet(grp, headers, args):
    Ncols, Nrows = headers['no. variables'], headers['no. points']

    if 'data' in grp:
        del grp['data']

    # Created a compressed dataset which can be re-sized to add more columns
    dset = grp.create_dataset('data',
                              dtype=_flags[headers['flags']],
                              shape=[Nrows, Ncols],
                              maxshape=[Nrows, None],
                              chunks=True, # auto-chunk [Nrows, 1],
                              shuffle=True,
                              compression='gzip')

    grp.attrs['formatid'] = 'spice2hdf-1.0'
    grp.attrs['columns'] = [V[0] for V in headers['variables']]
    grp.attrs['coltypes'] = [V[1] for V in headers['variables']]
    for H in ['title','date','plotname']: # white list of headers to include
        if H in headers:
            grp.attrs[H] = headers[H]

    return dset

def createMemSet(headers):
    Ncols, Nrows = headers['no. variables'], headers['no. points']

    return np.ndarray([Nrows, Ncols], dtype=_flags[headers['flags']])

def readBinary(inp, out):
    Ncol = out.shape[1]
    # on disk is little endian (always?)
    Ftype = out.dtype.newbyteorder('<')
    itemsize = Ftype.itemsize

    N = 0
    while True:
        # read binary data one column at a time
        raw = inp.read(Ncol*itemsize)
        if len(raw)==0:
            return # end of file
        elif len(raw)<Ncol*itemsize:
            _L.warn('Found partial column at end of file (%d, %d)',
                    len(raw), Ncol*itemsize)
            return

        out[N,:] = np.fromstring(raw, dtype=Ftype)
        N += 1

    if N<out.shape[0]:
        _L.error('Unexpected end of data (%d,%d)', N, out.shape[0])

def readAscii(inp, out):
    Nrow, Ncol = out.shape[:]
    comp = out.dtype.kind=='c'

    Nc, Nr = 0, 0
    for L in inp.readlines():
        if not L.strip():
            continue
        if Nc==0:
            # expect to start a new row (and read the row number)
            X, val = L.split(None, 1)
            assert int(X)==Nr, "Row id doesn't match(%s,%d)"%(X,Nr)
        else:
            val = L
        if not comp:
            val = float(val)
        else:
            val = np.complex(*map(float, val.split(',',1)))
        out[Nr,Nc] = val
        Nc += 1
        if Nc==Ncol:
            Nc, Nr = 0, Nr+1

    if (Nr, Nc)!=(Nrow,0):
        _L.error('Unexpected end of data (%d,%d) != (%d,%d)', Nr, Nc, Nrow, 0)

def loadspice(inp):
    """Read a spice output file into memory

    Returns a tuple (data, headers)

    Where data is a numpy array and headers
    is a dictionary containing entries from the
    output file header
    """
    head = readHeader(inp)
    OS = createMemSet(head)
    if 'binary' in head:
        readBinary(inp, OS)
    elif 'values' in head:
        readAscii(inp, OS)
    else:
        raise ValueError('Missing format tag')
    return OS, head

def main(args):
    head = readHeader(args.infile)
    OS = createOutputSet(args.outfile, head, args)
    if 'binary' in head:
        readBinary(args.infile, OS)
    elif 'values' in head:
        readAscii(args.infile, OS)
    else:
        raise ValueError('Missing format tag')
