# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import os

from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from .ui_projectedit import Ui_ProjEdit

class ProjEdit(QtGui.QMainWindow):
    def __init__(self, item, parent=None):
        self.item = item
        QtGui.QMainWindow.__init__(self, parent)
        self.setAttribute(Qt.WA_DeleteOnClose, False)
        
        self.ui = Ui_ProjEdit()
        self.ui.setupUi(self)

        self.fload = QtGui.QFileDialog(self,
                                       "Load Netlist",
                                       os.getcwd(),
                                       "Net/Schematic (*.net *.sch);;All files (*)")
        self.fload.setFileMode(QtGui.QFileDialog.ExistingFile)

        self.ui.fileBtn.clicked.connect(self.fload.show)
        self.fload.fileSelected.connect(self.ui.fileName.setEditText)

        self.ui.fileType.addItems(["Load Netlist","Generate from Schematic"])
        self.ui.fileType.setCurrentIndex(1)

        applybtn = self.ui.btnbox.button(self.ui.btnbox.Apply)
        applybtn.setShortcut("Shift+Return")

        self.ui.btnbox.clicked.connect(self.click)

        self.setWindowTitle("Project")

    def click(self, btn):
        if not btn:
            return
        role = self.ui.btnbox.buttonRole(btn)
        if role==self.ui.btnbox.ApplyRole:
            self.apply()
        elif role==self.ui.btnbox.ResetRole:
            self.reset()

    def apply(self):
        self.item.fname = str(self.ui.fileName.currentText())
        self.item.genNet = self.ui.fileType.currentIndex()==1

    def reset(self):
        self.ui.fileName.setEditText(self.item.fname)
        idx = 0
        if self.item.genNet:
            idx = 1
        self.ui.fileType.setCurrentIndex(idx)

