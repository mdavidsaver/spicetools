# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simedit.ui'
#
# Created: Sun Apr 20 16:15:49 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SimEdit(object):
    def setupUi(self, SimEdit):
        SimEdit.setObjectName(_fromUtf8("SimEdit"))
        SimEdit.resize(444, 178)
        self.centralwidget = QtGui.QWidget(SimEdit)
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
        SimEdit.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(SimEdit)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SimEdit.setStatusBar(self.statusbar)

        self.retranslateUi(SimEdit)
        QtCore.QMetaObject.connectSlotsByName(SimEdit)

    def retranslateUi(self, SimEdit):
        SimEdit.setWindowTitle(QtGui.QApplication.translate("SimEdit", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SimEdit", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SimEdit", "Directive", None, QtGui.QApplication.UnicodeUTF8))

