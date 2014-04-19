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

        self.menus = {}
        self.activeItem = None

        M = self.menus['vars'] = QtGui.QMenu(self)
        M.addAction("Expression").setEnabled(False)
        M.addSeparator()
        M.addAction("&Show", self.raiseExpr)
        M.addAction("&New", self.newExpr)
        M.addAction("&Remove", self.delExpr)

    def showProjectMenu(self, pt):
        idx = self.ui.projectView.indexAt(pt)
        if not idx.isValid():
            return

        item = self.model.itemFromIndex(idx)
        M = self.menus.get(getattr(item, 'itype', None), None)
        if not M:
            return

        print 'Show menu at',pt,item
        M.exec_(self.mapToGlobal(pt))

    def editExpr(self):
        pass
    def newExpr(self):
        pass
    def delExpr(self):
        pass
