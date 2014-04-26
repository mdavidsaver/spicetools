# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

def main():
    import sys, logging
    from PyQt4 import QtGui as gui
    from .simwin import SimWin
    from .util import TempDir

    logging.basicConfig(format="%(asctime)s %(message)s",
                        level=logging.DEBUG)

    app = gui.QApplication(sys.argv)
    args = app.arguments()
    wins = []
    if len(args)>1:
        for F in args[1:]:
            Q = SimWin()
            Q.open(F)
            wins.append(Q)
    else:
        wins.append(SimWin())
    for W in wins:
        W.show()

    try:
        sys.exit(app.exec_())
    finally:
        TempDir.cleanup()
