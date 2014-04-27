# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import unittest

from PyQt4 import QtCore, QtGui

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = QtGui.QApplication([])
    def tearDown(self):
        import weakref
        R = weakref.ref(self.app)
        # ensure QApplication is completely gone.
        # avoids a segfault when the interpreter shuts down.
        self.app = None
        import gc
        gc.collect()
        self.assertIs(None, R())


class SigRecorder(QtCore.QObject):
    def __init__(self, *args):
        super(SigRecorder,self).__init__(*args)
        self.clear()
    def clear(self):
        self.S = []
    @QtCore.pyqtSlot()
    def empty(self):
        self.S.append(None)
    @QtCore.pyqtSlot(QtCore.QString)
    def string(self, S):
        self.S.append(S)
    @QtCore.pyqtSlot(bool)
    def boolean(self, S):
        self.S.append(S)
