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

        S = self.ui.mdi.addSubWindow(self.root.win)
        S.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        self.root.win.setParent(S)
        S.hide()

        self.dclk = {
            'project':self.showProject,
            'calc':self.showExpr,
        }

        self.menus = {}
        self.activeItem = None

        M = self.menus['project'] = QtGui.QMenu(self)
        M.addAction("&Show", self.showProject)

        M = self.menus['vars'] = QtGui.QMenu(self)
        M.addAction("Expression").setEnabled(False)
        M.addSeparator()
        M.addAction("&New", self.newExpr)

        M = self.menus['calc'] = QtGui.QMenu(self)
        M.addAction("Expression").setEnabled(False)
        M.addSeparator()
        M.addAction("&Show", self.showExpr)
        M.addAction("&New", self.newExpr)
        M.addAction("&Delete", self.delExpr)

        M = self.menus['sims'] = QtGui.QMenu(self)
        M.addAction("Analysis").setEnabled(False)
        M.addSeparator()
        M.addAction("&New", self.newSim)

        M = self.menus['sim'] = QtGui.QMenu(self)
        M.addAction("Analysis").setEnabled(False)
        M.addSeparator()
        M.addAction("&Show", self.showSim)
        M.addAction("&New", self.newSim)
        M.addAction("&Delete", self.delSim)

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

    def showProject(self):
        self.root.win.show()

    def _addSubWin(self, win):
        S = self.ui.mdi.addSubWindow(win)
        S.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        win.setParent(S)
        win.show()

    _iopts = [
        # name, factory, iparent, inode)
        ('Calc', project.Calc, 'vars', 'calc'),
        ('Sim', project.Sim, 'sims', 'sim'),
    ]
    def new_X(self, F,P,I):
        assert self.activeItem.itype in [P,I]

        E = F()

        if self.activeItem.itype==P:
            self.activeItem.appendRow(E)
        else:
            parent = self.activeItem.parent()
            assert parent and parent.itype==P
            parent.insertRow(self.activeItem.row(), E)

        self._addSubWin(E.win)
        

    def newExpr(self):
        return self.new_X(project.Calc, 'vars', 'calc')

    def newSim(self):
        return self.new_X(project.Sim, 'sims', 'sim')

    def show_X(self, I):
        assert self.activeItem.itype==I

        S = self.activeItem.win.parentWidget()
        if S:
            self.activeItem.win.show()
            self.ui.mdi.setActiveSubWindow(S)
            return

        self._addSubWin(self.activeItem.win)

    def showExpr(self):
        return self.show_X('calc')

    def showSim(self):
        return self.show_X('sim')

    def del_X(self, I):
        assert self.activeItem.itype==I
        I = self.activeItem

        S = I.win.parentWidget()
        assert I.win.item is I
        I.win.item = None
        I.win = None

        self.ui.mdi.removeSubWindow(S)
        S.deleteLater() # delete S and I.win

        I.parent().removeRow(I.row())
        # I is deleted

        self.activeItem = None # be explicit

    def delExpr(self):
        return self.del_X('calc')

    def delSim(self):
        return self.del_X('sim')
