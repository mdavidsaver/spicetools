# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spicetools/bench/analysis.ui'
#
# Created: Mon Jul  7 06:29:33 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Analysis(object):
    def setupUi(self, Analysis):
        Analysis.setObjectName(_fromUtf8("Analysis"))
        Analysis.resize(398, 239)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Analysis.sizePolicy().hasHeightForWidth())
        Analysis.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Analysis)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Analysis)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.name = QtGui.QLineEdit(Analysis)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout_2.addWidget(self.name)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnDel = QtGui.QPushButton(Analysis)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.horizontalLayout_2.addWidget(self.btnDel)
        self.btnHide = QtGui.QPushButton(Analysis)
        self.btnHide.setCheckable(True)
        self.btnHide.setChecked(True)
        self.btnHide.setObjectName(_fromUtf8("btnHide"))
        self.horizontalLayout_2.addWidget(self.btnHide)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget = QtGui.QWidget(Analysis)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.beforeText = QtGui.QPlainTextEdit(self.widget)
        self.beforeText.setObjectName(_fromUtf8("beforeText"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.beforeText)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.sim = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sim.sizePolicy().hasHeightForWidth())
        self.sim.setSizePolicy(sizePolicy)
        self.sim.setObjectName(_fromUtf8("sim"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sim)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.afterText = QtGui.QPlainTextEdit(self.widget)
        self.afterText.setObjectName(_fromUtf8("afterText"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.afterText)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Analysis)
        QtCore.QObject.connect(self.btnHide, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Analysis)

    def retranslateUi(self, Analysis):
        Analysis.setWindowTitle(QtGui.QApplication.translate("Analysis", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Analysis", "Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.name.setPlaceholderText(QtGui.QApplication.translate("Analysis", "name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDel.setText(QtGui.QApplication.translate("Analysis", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHide.setText(QtGui.QApplication.translate("Analysis", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Analysis", "Before:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Analysis", "Sim:", None, QtGui.QApplication.UnicodeUTF8))
        self.sim.setPlaceholderText(QtGui.QApplication.translate("Analysis", "analysis definition", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Analysis", "After:", None, QtGui.QApplication.UnicodeUTF8))

