# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expr.ui'
#
# Created: Sat Apr 26 15:54:51 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Expr(object):
    def setupUi(self, Expr):
        Expr.setObjectName(_fromUtf8("Expr"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Expr.sizePolicy().hasHeightForWidth())
        Expr.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Expr)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Expr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.btnDel = QtGui.QPushButton(Expr)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.horizontalLayout_2.addWidget(self.btnDel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Expr)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.name = QtGui.QLineEdit(Expr)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout.addWidget(self.name)
        self.label_3 = QtGui.QLabel(Expr)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.expr = QtGui.QLineEdit(Expr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expr.sizePolicy().hasHeightForWidth())
        self.expr.setSizePolicy(sizePolicy)
        self.expr.setObjectName(_fromUtf8("expr"))
        self.horizontalLayout.addWidget(self.expr)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Expr)
        QtCore.QMetaObject.connectSlotsByName(Expr)

    def retranslateUi(self, Expr):
        Expr.setWindowTitle(QtGui.QApplication.translate("Expr", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Expr", "Expression", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDel.setText(QtGui.QApplication.translate("Expr", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Expr", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.name.setPlaceholderText(QtGui.QApplication.translate("Expr", "name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Expr", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.expr.setPlaceholderText(QtGui.QApplication.translate("Expr", "expression", None, QtGui.QApplication.UnicodeUTF8))

