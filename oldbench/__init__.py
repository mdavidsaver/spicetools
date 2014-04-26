# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

def main():
    import sys
    from PyQt4 import QtGui as gui
    from .simmain import SimWindow
    app = gui.QApplication(sys.argv)
    win = SimWindow()
    win.show()
    return app.exec_()

