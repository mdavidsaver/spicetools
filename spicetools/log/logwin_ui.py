# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spicetools/log/logwin.ui'
#
# Created: Sun Apr 27 15:19:31 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LogWin(object):
    def setupUi(self, LogWin):
        LogWin.setObjectName(_fromUtf8("LogWin"))
        LogWin.resize(709, 308)
        self.centralwidget = QtGui.QWidget(LogWin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.log = QtGui.QTextEdit(self.centralwidget)
        self.log.setReadOnly(True)
        self.log.setObjectName(_fromUtf8("log"))
        self.verticalLayout.addWidget(self.log)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.errCnt = QtGui.QLabel(self.centralwidget)
        self.errCnt.setObjectName(_fromUtf8("errCnt"))
        self.horizontalLayout.addWidget(self.errCnt)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.autoClr = QtGui.QCheckBox(self.centralwidget)
        self.autoClr.setChecked(True)
        self.autoClr.setObjectName(_fromUtf8("autoClr"))
        self.horizontalLayout.addWidget(self.autoClr)
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.horizontalLayout.addWidget(self.btnClear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        LogWin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(LogWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        LogWin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(LogWin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LogWin.setStatusBar(self.statusbar)
        self.actionSaveAs = QtGui.QAction(LogWin)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionClose = QtGui.QAction(LogWin)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionClear = QtGui.QAction(LogWin)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.menu_File.addAction(self.actionSaveAs)
        self.menu_File.addAction(self.actionClear)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionClose)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(LogWin)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), LogWin.close)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionClear.trigger)
        QtCore.QMetaObject.connectSlotsByName(LogWin)

    def retranslateUi(self, LogWin):
        LogWin.setWindowTitle(QtGui.QApplication.translate("LogWin", "Spice Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LogWin", "Errors:", None, QtGui.QApplication.UnicodeUTF8))
        self.errCnt.setText(QtGui.QApplication.translate("LogWin", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.autoClr.setText(QtGui.QApplication.translate("LogWin", "Auto Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("LogWin", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("LogWin", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("LogWin", "&Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("LogWin", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("LogWin", "&Clear", None, QtGui.QApplication.UnicodeUTF8))

