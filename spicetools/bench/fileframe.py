# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import os, os.path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

from .fileframe_ui import Ui_FileFrame

class FileFrame(QtGui.QFrame):
    fileChanged = QtCore.pyqtSignal(QtCore.QString)
    typeChanged = QtCore.pyqtSignal(bool)

    def __init__(self, parent):
        super(FileFrame, self).__init__(parent)
        
        self.ui = Ui_FileFrame()
        self.ui.setupUi(self)

        self.dia = QtGui.QFileDialog(self, "Select Net of Schem.",
                                     os.getcwd(),
                                     "Net/Schem. (*.net *.sch);;All (*)")
        self.dia.setFileMode(self.dia.ExistingFile)

        self.ui.fileBtn.clicked.connect(self.dia.show)
        self.dia.fileSelected.connect(self.setFile)
        self.ui.fileBox.activated.connect(self._fileChange)

        self.ui.typeBox.currentIndexChanged.connect(self._typeChanged)

    def clear(self):
        self.setFile('')
        self.setType(True)

    def _fileChange(self):
        self.fileChanged.emit(self.ui.fileBox.currentText())

    def _typeChanged(self, i):
        self.typeChanged.emit(i==1)

    def setFile(self, fname):
        self.ui.fileBox.setEditText(fname)
        self.fileChanged.emit(fname)

    def setType(self, B):
        self.ui.typeBox.setCurrentIndex(1 if B else 0)

    def file(self):
        return self.ui.fileBox.currentText()

    def type(self):
        return self.ui.typeBox.currentIndex()==1

    file = QtCore.pyqtProperty(QtCore.QString, file, setFile,
                               notify=fileChanged)

    type = QtCore.pyqtProperty(bool, type, setType,
                               notify=typeChanged)
