# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from PyQt4 import QtCore, QtGui

from ..util import svarname

from .dnd import DragAndDropMixin

from .analysis_ui import  Ui_Analysis

beforetip = """alter Inst Value
alter Inst Param=Value
alter Inst Param=Value Param=Value ...
"""

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

aftertip = """let Var = Expr
"""

class Analysis(QtGui.QWidget, DragAndDropMixin):
    nameChanged = QtCore.pyqtSignal(QtCore.QString)
    simChanged = QtCore.pyqtSignal(QtCore.QString)
    beforeChanged = QtCore.pyqtSignal(QtCore.QString)
    afterChanged = QtCore.pyqtSignal(QtCore.QString)

    def __init__(self, parent):
        super(Analysis, self).__init__(parent)
        self.setAcceptDrops(True)

        self.ui = Ui_Analysis()
        self.ui.setupUi(self)

        self.ui.btnDel.clicked.connect(self.deleteLater)

        self.ui.name.setValidator(QtGui.QRegExpValidator(svarname, self.ui.name))
        self.ui.beforeText.setToolTip(beforetip)
        self.ui.sim.setToolTip(simtip)
        self.ui.afterText.setToolTip(aftertip)

    def name(self):
        return self.ui.name.text()

    def sim(self):
        return self.ui.sim.text()

    def before(self):
        return self.ui.beforeText.toPlainText()

    def after(self):
        return self.ui.afterText.toPlainText()

    def setName(self, S):
        self.ui.name.setText(S)
        self.nameChanged.emit(S)

    def setSim(self, S):
        self.ui.sim.setText(S)
        self.simChanged.emit(S)

    def setBefore(self, S):
        self.ui.beforeText.setPlainText(S)
        self.beforeChanged.emit(S)

    def setAfter(self, S):
        self.ui.afterText.setPlainText(S)
        self.afterChanged.emit(S)

    def dropEvent(self, evt):
        if not self.canDrop(evt):
            return
        S = evt.source()

        # Analysis in our place
        I = self.parent().layout().indexOf(self)

        S = evt.source()
        S.parent().layout().removeWidget(S)
        S.setParent(self.parent())
        self.parent().layout().insertWidget(I, S)
        S._level = self._level
            
        evt.acceptProposedAction()

Analysis.acceptableDrops = (Analysis,)
