# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from PyQt4 import QtGui

from .ui_varedit import Ui_VarEdit

class VarEdit(QtGui.QMainWindow):
    def __init__(self, item, parent=None):
        self.item = item
        QtGui.QMainWindow.__init__(self, parent)
        
        self.ui = Ui_VarEdit()
        self.ui.setupUi(self)

        self.ui.btnbox.clear()
        self.ui.btnbox.clicked.connect(self.click)

        self.setWindowTitle("Expr - %"%self.item.name)

    def click(self, btn):
        if not btn:
            return
        role = self.ui.btnbox.buttonRole(btn)
        if role==self.ui.btnbox.ApplyRole:
            self.apply()
        elif role==self.ui.btnbox.ResetRole:
            self.reset()
        self.setWindowTitle("Expr - %"%self.item.name)

    def apply(self):
        self.item.update(str(self.ui.name.text(),
                         str(self.ui.expr.toPlainText())))

    def reset(self):
        self.ui.name.setText(self.item.name)
        self.ui.expr.setPlainText(self.item.expr)

