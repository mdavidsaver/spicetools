# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

__all__ = [
    'h5group',
    'addCommonArgs',
    'runCLI',
    'runGUI',
]

class UserError(Exception):
    pass

def h5group(**kws):
    """Process file:group/path and return a writable H5PY Group object

    Suitable for use with the argparse module.
    
    parser.add_argument('outfile', type=h5group())
    """
    import h5py
    def typer(h5str):
        if h5str=='<<<skip>>>':
            return None
        fname, _, path = h5str.partition(':')
        try:
            H = h5py.File(fname, **kws)
        except:
            print "Error opening",fname,path
            raise
        if path:
            return H.require_group(path)
        else:
            return H
    return typer

def addCommonArgs(P):
    """Add common arguments to ArgumentParser

    Adds options 'verbose' which stores a logging module level,
    and 'format' which stores a logging module format string.
    Together these are suitable to pass to :py:func`logging.basicConfig`.

    >>> import logging, argparse
    >>> P = argparse.ArgumentParser()
    >>> addCommonArgs(P)
    >>> opts = P.parse_args([])
    >>> opts.level==logging.INFO
    True
    >>> opts.format
    '%(message)s'
    >>> opts = P.parse_args(['--time','-v'])
    >>> opts.level==logging.DEBUG
    True
    >>> opts.format
    '%(asctime)s %(message)s'
    >>> opts = P.parse_args(['-q'])
    >>> opts.level==logging.WARN
    True
    >>> opts.format
    '%(message)s'
    """
    import logging
    P.add_argument('--verbose', '-v', dest='level', action='store_const',
                   default=logging.INFO, const=logging.DEBUG,
                   help="Make more noise")
    P.add_argument('--quiet', '-q', dest='level', action='store_const',
                   const=logging.WARN,
                   help="Make less noise")
    P.add_argument('--time', dest='format', action='store_const',
                   default='%(message)s', const='%(asctime)s %(message)s',
                   help="Include current time in output lines")

def runCLI(mod):
    """Run a command line application

    'mod' must provide a method 'getargs' which returns
    an ArgumentParser, and a method 'main' which accepts
    an parsed arguments object.
    """
    opts = mod.getargs().parse_args()
    import logging
    logging.basicConfig(level=opts.level, format=opts.format)

    from .util import TempDir
    try:
        mod.main(opts)
    except UserError as e:
        logging.error('Error: %s:'%e.message)
    finally:
        TempDir.cleanup()

def runGUI(mod):
    """Run a Qt graphical application

    'mod' must provide a method 'getargs' which returns
    an ArgumentParser, and a method 'window' which accepts
    an parsed arguments object and returns a list of QWidgets.
    """
    P = mod.getargs()
    import sys, logging
    from PyQt4 import QtGui
    app = QtGui.QApplication(sys.argv)
    opts = P.parse_args(map(str, app.arguments()[1:]))

    logging.basicConfig(level=opts.level, format=opts.format)

    wins = []
    if opts.infile:
        if isinstance(opts.infile, list):
            for F in opts.infile:
                W = mod.window()
                W.open(F)
                wins.append(W)
        else:
            W = mod.window()
            W.open(opts.infile)
            wins.append(W)
    else:
        wins.append(mod.window())
    [W.show() for W in wins]
    from .util import TempDir
    try:
        sys.exit(app.exec_())
    finally:
        TempDir.cleanup()

if __name__=='__main__':
    import doctest
    doctest.testmod()
