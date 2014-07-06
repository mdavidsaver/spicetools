# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

from ..util import svarname

from .expr import Expr, Alter
from .dnd import DragAndDropMixin

from .analysis_ui import  Ui_Analysis

simtip = """tran Tstep Tstop [ Tstart [ Tmax ] ] [ UIC ]
dc Source Vstart Vstop Vincr [ Source2 Vstart2 Vstop2 Vincr2 ]
ac DEC|OCT|LIN ) N Fstart Fstop
op
tf Node Source
pz Node Node Node Node cur|vol pol|zer|pz
sens Var
sens Var ac DEC|OCT|LIN N Fstart Fstop
noise Node Source DEC|OCT|LIN N Fstart Fstop
disto DEC|OCT|LIN ) N Fstart Fstop
"""

class Analysis(QtGui.QWidget, DragAndDropMixin):
    nameChanged = QtCore.pyqtSignal(QtCore.QString)
    simChanged = QtCore.pyqtSignal(QtCore.QString)

    def __init__(self, parent):
        super(Analysis, self).__init__(parent)
        self.setAcceptDrops(True)

        self.ui = Ui_Analysis()
        self.ui.setupUi(self)

        QtGui.QVBoxLayout(self.ui.frame)
        self.ui.frame.layout().insertStretch(0)

        self.ui.btnDel.clicked.connect(self.deleteLater)
        self.ui.btnExpr.clicked.connect(self.addExpr)
        self.ui.btnAlter.clicked.connect(self.addAlter)

        self.ui.name.setValidator(QtGui.QRegExpValidator(svarname, self.ui.name))
        self.ui.sim.setToolTip(simtip)

    def name(self):
        return self.ui.name.text()

    def setName(self, S):
        self.ui.name.setText(S)
        self.nameChanged.emit(S)

    def setSim(self, S):
        self.ui.sim.setText(S)
        self.simChanged.emit(S)

    def sim(self):
        return self.ui.sim.text()

    name = QtCore.pyqtProperty(QtCore.QString, name, setName, notify=nameChanged)
    sim = QtCore.pyqtProperty(QtCore.QString, sim, setSim, notify=simChanged)

    def exprWidget(self):
        return self.ui.frame

    def addExpr(self):
        E = Expr(self.ui.frame)
        E._level = self._level + 1
        self.ui.frame.layout().insertWidget(0,E)

    def addAlter(self):
        E = Alter(self.ui.frame)
        E._level = self._level + 1
        self.ui.frame.layout().insertWidget(0,E)

    def dropEvent(self, evt):
        if not self.canDrop(evt):
            return
        S = evt.source()

        if isinstance(S, (Expr,Alter)) and self.ui.frame.geometry().contains(evt.pos()):
            # drop Expr/Alter into analysis
            S.parent().layout().removeWidget(S)
            S.setParent(self.ui.frame)
            self.ui.frame.layout().insertWidget(0,S)
            S._level = self._level + 1

        else:
            # drop Expr, Alter, or Analysis in our place
            I = self.parent().layout().indexOf(self)
    
            S = evt.source()
            S.parent().layout().removeWidget(S)
            S.setParent(self.parent())
            self.parent().layout().insertWidget(I, S)
            S._level = self._level
            
        evt.acceptProposedAction()

Analysis.acceptableDrops = (Analysis, Expr, Alter)
Expr.acceptableDrops = Expr.acceptableDrops + (Analysis,)
Alter.acceptableDrops = Alter.acceptableDrops + (Analysis,)
