# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import unittest

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtTest import QTest

from ..fileframe import FileFrame

from .tutil import SigRecorder, AppTestCase

class TestFileFrame(AppTestCase):
    def setUp(self):
        super(TestFileFrame, self).setUp()
        self.main = QtGui.QWidget()
        self.F = FileFrame(self.main)        

    def test_prop(self):
        self.assertEqual('', str(self.F.file))

        R = SigRecorder()
        self.F.fileChanged.connect(R.string)

        self.F.file = 'hello'

        self.assertEqual('hello', self.F.file)
        self.assertEqual(['hello'], R.S)

    def test_enter(self):
        R = SigRecorder()
        self.F.fileChanged.connect(R.string)

        #self.F.ui.fileBox.setFocus(Qt.MouseFocusReason)
        QTest.keyClicks(self.F.ui.fileBox, "testing")
        QTest.keyClick(self.F.ui.fileBox, Qt.Key_Enter)

        self.assertEqual('testing', str(self.F.file))
        self.assertEqual(['testing'], R.S)
        R.clear()

        self.assertEqual(1, self.F.ui.fileBox.count())
        self.assertEqual('testing', self.F.ui.fileBox.itemText(0))

        for n in range(7):
            QTest.keyClick(self.F.ui.fileBox, Qt.Key_Backspace)
        QTest.keyClicks(self.F.ui.fileBox, "another")
        QTest.keyClick(self.F.ui.fileBox, Qt.Key_Enter)

        self.assertEqual('another', str(self.F.file))
        self.assertEqual(['another'], R.S)

        self.assertEqual(2, self.F.ui.fileBox.count())
        self.assertEqual('another', self.F.ui.fileBox.itemText(0))
        self.assertEqual('testing', self.F.ui.fileBox.itemText(1))

if __name__=='__main__':
    unittest.main()
