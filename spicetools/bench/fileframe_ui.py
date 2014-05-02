# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spicetools/bench/fileframe.ui'
#
# Created: Sun Apr 27 13:13:00 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FileFrame(object):
    def setupUi(self, FileFrame):
        FileFrame.setObjectName(_fromUtf8("FileFrame"))
        FileFrame.resize(270, 37)
        FileFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        FileFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(FileFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.typeBox = QtGui.QComboBox(FileFrame)
        self.typeBox.setObjectName(_fromUtf8("typeBox"))
        self.typeBox.addItem(_fromUtf8(""))
        self.typeBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.typeBox)
        self.label = QtGui.QLabel(FileFrame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.fileBox = QtGui.QComboBox(FileFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileBox.sizePolicy().hasHeightForWidth())
        self.fileBox.setSizePolicy(sizePolicy)
        self.fileBox.setEditable(True)
        self.fileBox.setMaxCount(10)
        self.fileBox.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.fileBox.setObjectName(_fromUtf8("fileBox"))
        self.horizontalLayout.addWidget(self.fileBox)
        self.fileBtn = QtGui.QPushButton(FileFrame)
        self.fileBtn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.fileBtn.setObjectName(_fromUtf8("fileBtn"))
        self.horizontalLayout.addWidget(self.fileBtn)

        self.retranslateUi(FileFrame)
        self.typeBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FileFrame)

    def retranslateUi(self, FileFrame):
        FileFrame.setWindowTitle(QtGui.QApplication.translate("FileFrame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.typeBox.setItemText(0, QtGui.QApplication.translate("FileFrame", "Net List", None, QtGui.QApplication.UnicodeUTF8))
        self.typeBox.setItemText(1, QtGui.QApplication.translate("FileFrame", "Schematic", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FileFrame", "File:", None, QtGui.QApplication.UnicodeUTF8))
        self.fileBtn.setText(QtGui.QApplication.translate("FileFrame", "<-", None, QtGui.QApplication.UnicodeUTF8))

