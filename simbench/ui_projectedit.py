# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectedit.ui'
#
# Created: Sun Apr 20 16:06:18 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProjEdit(object):
    def setupUi(self, ProjEdit):
        ProjEdit.setObjectName(_fromUtf8("ProjEdit"))
        ProjEdit.resize(300, 110)
        self.centralwidget = QtGui.QWidget(ProjEdit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fileName = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileName.sizePolicy().hasHeightForWidth())
        self.fileName.setSizePolicy(sizePolicy)
        self.fileName.setEditable(True)
        self.fileName.setMaxCount(10)
        self.fileName.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.horizontalLayout.addWidget(self.fileName)
        self.fileBtn = QtGui.QPushButton(self.centralwidget)
        self.fileBtn.setObjectName(_fromUtf8("fileBtn"))
        self.horizontalLayout.addWidget(self.fileBtn)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.fileType = QtGui.QComboBox(self.centralwidget)
        self.fileType.setObjectName(_fromUtf8("fileType"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.fileType)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.btnbox = QtGui.QDialogButtonBox(self.centralwidget)
        self.btnbox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Reset)
        self.btnbox.setObjectName(_fromUtf8("btnbox"))
        self.verticalLayout.addWidget(self.btnbox)
        ProjEdit.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ProjEdit)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ProjEdit.setStatusBar(self.statusbar)

        self.retranslateUi(ProjEdit)
        QtCore.QMetaObject.connectSlotsByName(ProjEdit)

    def retranslateUi(self, ProjEdit):
        ProjEdit.setWindowTitle(QtGui.QApplication.translate("ProjEdit", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProjEdit", "File name:", None, QtGui.QApplication.UnicodeUTF8))
        self.fileBtn.setText(QtGui.QApplication.translate("ProjEdit", "<-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProjEdit", "File Type:", None, QtGui.QApplication.UnicodeUTF8))

