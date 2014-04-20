# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import os, os.path, tempfile

from PyQt4 import QtCore, QtGui

from .ui_simmain import Ui_MainWindow

from . import project

_gnetlist = "gnetlist -g spice-sdb -O include_mode -O nomunge_mode -o %(net)s %(sch)s"

simtip = """tran Tstep Tstop [ Tstart [ Tmax ] ] [ UIC ]
dc Source-Name Vstart Vstop Vincr [ Source2 Vstart2 Vstop2 Vincr2 ]
ac ( DEC | OCT | LIN ) N Fstart Fstop
op
"""

class SimWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.psave = QtGui.QFileDialog(self,
                                       "Save Project",
                                       os.getcwd(),
                                       "Project (*.sprj);;All files (*)")
        self.psave.setDefaultSuffix(".sprj")

        self.ui.actionSave.triggered.connect(self.psave.show)


        self.pselect = QtGui.QFileDialog(self,
                                       "Save Project",
                                       os.getcwd(),
                                       "Project (*.sprj);;All files (*)")
        self.pselect.setFileMode(QtGui.QFileDialog.ExistingFile)

        self.ui.actionOpen.triggered.connect(self.pselect.show)

        app = QtGui.QApplication.instance()
        self.ui.actionQuit.triggered.connect(app.quit)

        self.setWindowTitle('Spice Simulation Workbench')

        self.root = project.Project()
        self.model = QtGui.QStandardItemModel()
        self.model.insertColumn(0, [self.root])
        self.model.setHorizontalHeaderLabels(['Name'])

        self.ui.projectView.setModel(self.model)

        self.ui.projectView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.projectView.customContextMenuRequested.connect(self.showProjectMenu)
        self.ui.projectView.doubleClicked.connect(self.projectDClick)

        self.dclk = {
            'vars':self.newExpr,
            'calc':self.showExpr,
        }

        self.menus = {}
        self.activeItem = None

        M = self.menus['vars'] = QtGui.QMenu(self)
        M.addAction("Expression").setEnabled(False)
        M.addSeparator()
        M.addAction("&New", self.newExpr)

        M = self.menus['calc'] = QtGui.QMenu(self)
        M.addAction("Expression").setEnabled(False)
        M.addSeparator()
        M.addAction("&Edit", self.showExpr)
        M.addAction("&New", self.newExpr)
        M.addAction("&Delete", self.delExpr)

    def projectDClick(self, idx):
        item = self.model.itemFromIndex(idx)

        M = self.dclk.get(getattr(item, 'itype', None), None)
        if not M:
            return
        self.activeItem = item
        try:
            M()
        finally:
            self.activeItem = None

    def showProjectMenu(self, pt):
        idx = self.ui.projectView.indexAt(pt)
        if not idx.isValid():
            return

        item = self.model.itemFromIndex(idx)
        M = self.menus.get(getattr(item, 'itype', None), None)
        if not M:
            return

        self.activeItem = item
        try:
            M.exec_(self.mapToGlobal(pt))
        finally:
            self.activeItem = None

    def newExpr(self):
        assert self.activeItem.itype in ['vars','calc']

        E = project.Calc()

        if self.activeItem.itype=='vars':
            self.activeItem.appendRow(E)
        else:
            P = self.activeItem.parent()
            assert P and P.itype=='vars'
            P.insertRow(self.activeItem.row(), E)

        S = self.ui.mdi.addSubWindow(E.win)
        S.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        E.win.setParent(S)

        E.win.show()

    def showExpr(self):
        assert self.activeItem.itype=='calc'

        S = self.activeItem.win.parentWidget()
        if S:
            self.activeItem.win.show()
            self.ui.mdi.setActiveSubWindow(S)
            return

        S = self.ui.mdi.addSubWindow(self.activeItem.win)
        S.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        self.activeItem.win.setParent(S)

    def delExpr(self):
        assert self.activeItem.itype=='calc'
        I = self.activeItem

        S = I.win.parentWidget()

        I.win.setParent(None)

        self.ui.mdi.removeSubWindow(S)
        S.deleteLater()

        I.parent().removeRow(I.row())
