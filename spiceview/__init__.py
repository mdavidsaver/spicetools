# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging

def getargs(args=None):
    import sys, argparse

    P = argparse.ArgumentParser(description="Spice or HDF5 data file viewer")
    P.add_argument('infile', nargs='?', default=[], metavar='FILE',
                   help='SPICE raw file or HDF5 w/ optional group (eg "file.h5:/grp")')
    P.add_argument('--verbose', '-v', action='store_const', default=logging.INFO, const=logging.DEBUG)
    P.add_argument('--quiet', '-q', action='store_const', dest='verbose', const=logging.WARN)

    return P.parse_args(args or sys.argv[1:])

def main():
    import sys
    from PyQt4 import QtGui as gui
    from .mainwin import ViewerWindow
    app = gui.QApplication(sys.argv)
    args = getargs(map(str, app.arguments()[1:]))
    logging.basicConfig(level=args.verbose)
    win = ViewerWindow()
    
    if args.infile:
        win.openFile(args.infile)
    win.show()
    return app.exec_()
