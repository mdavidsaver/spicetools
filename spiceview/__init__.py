# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

def main():
    import sys
    from PyQt4 import QtGui as gui
    from .mainwin import ViewerWindow
    app = gui.QApplication(sys.argv)
    win = ViewerWindow()
    args = app.arguments()[1:]
    if len(args):
        win.openFile(args[0])
    win.show()
    return app.exec_()
