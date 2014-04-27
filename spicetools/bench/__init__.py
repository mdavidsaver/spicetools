# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

def getargs():
    import argparse
    from ..run import addCommonArgs

    P = argparse.ArgumentParser(description="Spice simulation controller")
    P.add_argument('infile', nargs='*', metavar='mysim.sprj',
                   help='.sprj file')
    addCommonArgs(P)
    return P

def window():
    from simwin import SimWin
    return SimWin()
