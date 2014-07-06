# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spicetools/bench/alter.ui'
#
# Created: Sat Jul  5 21:26:21 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Alter(object):
    def setupUi(self, Alter):
        Alter.setObjectName(_fromUtf8("Alter"))
        Alter.resize(296, 61)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Alter.sizePolicy().hasHeightForWidth())
        Alter.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Alter)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Alter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.name = QtGui.QLineEdit(Alter)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout_2.addWidget(self.name)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnDel = QtGui.QPushButton(Alter)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.horizontalLayout_2.addWidget(self.btnDel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(Alter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.expr = QtGui.QLineEdit(Alter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expr.sizePolicy().hasHeightForWidth())
        self.expr.setSizePolicy(sizePolicy)
        self.expr.setObjectName(_fromUtf8("expr"))
        self.horizontalLayout.addWidget(self.expr)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Alter)
        QtCore.QMetaObject.connectSlotsByName(Alter)

    def retranslateUi(self, Alter):
        Alter.setWindowTitle(QtGui.QApplication.translate("Alter", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Alter", "Alter", None, QtGui.QApplication.UnicodeUTF8))
        self.name.setPlaceholderText(QtGui.QApplication.translate("Alter", "name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDel.setText(QtGui.QApplication.translate("Alter", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Alter", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.expr.setToolTip(QtGui.QApplication.translate("Alter", "<html><head/><body><p>Value</p><p>Name=Value ...</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.expr.setPlaceholderText(QtGui.QApplication.translate("Alter", "expression", None, QtGui.QApplication.UnicodeUTF8))

