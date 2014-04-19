# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'varedit.ui'
#
# Created: Sat Apr 19 19:00:29 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VarEdit(object):
    def setupUi(self, VarEdit):
        VarEdit.setObjectName(_fromUtf8("VarEdit"))
        VarEdit.resize(444, 178)
        self.centralwidget = QtGui.QWidget(VarEdit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.name = QtGui.QLineEdit(self.centralwidget)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout.addWidget(self.name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.expr = QtGui.QPlainTextEdit(self.centralwidget)
        self.expr.setObjectName(_fromUtf8("expr"))
        self.verticalLayout.addWidget(self.expr)
        self.btnbox = QtGui.QDialogButtonBox(self.centralwidget)
        self.btnbox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Reset)
        self.btnbox.setObjectName(_fromUtf8("btnbox"))
        self.verticalLayout.addWidget(self.btnbox)
        VarEdit.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(VarEdit)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        VarEdit.setStatusBar(self.statusbar)

        self.retranslateUi(VarEdit)
        QtCore.QMetaObject.connectSlotsByName(VarEdit)

    def retranslateUi(self, VarEdit):
        VarEdit.setWindowTitle(QtGui.QApplication.translate("VarEdit", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("VarEdit", "Variable Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("VarEdit", "Expression", None, QtGui.QApplication.UnicodeUTF8))

