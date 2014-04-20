# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from .ui_varedit import Ui_VarEdit

class VarEdit(QtGui.QMainWindow):
    def __init__(self, item, parent=None):
        self.item = item
        QtGui.QMainWindow.__init__(self, parent)
        self.setAttribute(Qt.WA_DeleteOnClose, False)

        self.ui = Ui_VarEdit()
        self.ui.setupUi(self)

        applybtn = self.ui.btnbox.button(self.ui.btnbox.Apply)
        applybtn.setShortcut("Shift+Return")

        self.ui.btnbox.clicked.connect(self.click)

        self.setWindowTitle("Expr - %s"%self.item.name)

    def click(self, btn):
        if not btn:
            return
        role = self.ui.btnbox.buttonRole(btn)
        if role==self.ui.btnbox.ApplyRole:
            self.apply()
        elif role==self.ui.btnbox.ResetRole:
            self.reset()
        self.setWindowTitle("Expr - %s"%self.item.name)

    def apply(self):
        self.item.name = str(self.ui.name.text())
        self.item.expr = str(self.ui.expr.toPlainText())
        self.item.setText(self.item.name)

    def reset(self):
        self.ui.name.setText(self.item.name)
        self.ui.expr.setPlainText(self.item.expr)

