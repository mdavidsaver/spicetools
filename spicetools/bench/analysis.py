# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

from ..util import svarname

from .expr import Expr

from .ui_analysis import  Ui_Analysis

simtip = """tran Tstep Tstop [ Tstart [ Tmax ] ] [ UIC ]
dc Source-Name Vstart Vstop Vincr [ Source2 Vstart2 Vstop2 Vincr2 ]
ac ( DEC | OCT | LIN ) N Fstart Fstop
op
"""

class Analysis(QtGui.QWidget):
    nameChanged = QtCore.pyqtSignal(QtCore.QString)
    simChanged = QtCore.pyqtSignal(QtCore.QString)

    def __init__(self, parent):
        super(Analysis, self).__init__(parent)

        self.ui = Ui_Analysis()
        self.ui.setupUi(self)

        QtGui.QVBoxLayout(self.ui.frame)

        self.ui.btnDel.clicked.connect(self.deleteLater)
        self.ui.btnExpr.clicked.connect(self.addExpr)

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
        self.ui.frame.layout().insertWidget(0,E)
