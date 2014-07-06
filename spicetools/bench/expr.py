# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

from ..util import svarname
from .dnd import DragAndDropMixin

from .expr_ui import Ui_Expr
from .alter_ui import Ui_Alter

class Common(QtGui.QWidget, DragAndDropMixin):
    nameChanged = QtCore.pyqtSignal(QtCore.QString)
    exprChanged = QtCore.pyqtSignal(QtCore.QString)

    def __init__(self, parent):
        super(Common, self).__init__(parent)
        self.setAcceptDrops(True)

        self.ui = self.uic()
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

    def dropEvent(self, evt):
        from .analysis import Analysis
        S = evt.source()

        if isinstance(S, Analysis) and self._level>0:
            return # can't nest Analysis within Analysis

        I = self.parent().layout().indexOf(self)

        S.parent().layout().removeWidget(S)
        S.setParent(self.parent())
        self.parent().layout().insertWidget(I, S)
        S._level = self._level
            
        evt.acceptProposedAction()

class Expr(Common):
    uic = Ui_Expr

class Alter(Common):
    uic = Ui_Alter

Expr.acceptableDrops = (Expr,Alter)
Alter.acceptableDrops = (Expr,Alter)
