# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

def getargs():
    import argparse
    from ..run import addCommonArgs

    P = argparse.ArgumentParser(description="Spice or HDF5 data file viewer")
    P.add_argument('infile', nargs='*', default=[], metavar='FILE',
                   help='SPICE raw file or HDF5 w/ optional group (eg "file.h5:/grp")')
    addCommonArgs(P)
    return P

def window():
    from .mainwin import ViewerWindow
    return ViewerWindow()
