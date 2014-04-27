# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

from ..util import svarname

from .ui_expr import Ui_Expr

class Expr(QtGui.QWidget):
    nameChanged = QtCore.pyqtSignal(QtCore.QString)
    exprChanged = QtCore.pyqtSignal(QtCore.QString)

    def __init__(self, parent):
        super(Expr, self).__init__(parent)

        self.ui = Ui_Expr()
        self.ui.setupUi(self)

        self.ui.btnDel.clicked.connect(self.deleteLater)

        self.ui.name.setValidator(QtGui.QRegExpValidator(svarname, self.ui.name))

    def name(self):
        return self.ui.name.text()

    def setName(self, S):
        self.ui.name.setText(S)
        self.nameChanged.emit(S)

    def setExpr(self, S):
        self.ui.expr.setText(S)
        self.exprChanged.emit(S)

    def expr(self):
        return self.ui.expr.text()

    name = QtCore.pyqtProperty(QtCore.QString, name, setName, notify=nameChanged)
    expr = QtCore.pyqtProperty(QtCore.QString, expr, setExpr, notify=exprChanged)
