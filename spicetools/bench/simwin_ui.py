# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spicetools/bench/simwin.ui'
#
# Created: Sun Jul  6 20:53:30 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SimWin(object):
    def setupUi(self, SimWin):
        SimWin.setObjectName(_fromUtf8("SimWin"))
        SimWin.resize(529, 488)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/bench.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SimWin.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(SimWin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnSim = QtGui.QPushButton(self.centralwidget)
        self.btnSim.setObjectName(_fromUtf8("btnSim"))
        self.horizontalLayout.addWidget(self.btnSim)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnRun = QtGui.QPushButton(self.centralwidget)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.horizontalLayout.addWidget(self.btnRun)
        self.btnStop = QtGui.QPushButton(self.centralwidget)
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.horizontalLayout.addWidget(self.btnStop)
        self.btnPlot = QtGui.QPushButton(self.centralwidget)
        self.btnPlot.setObjectName(_fromUtf8("btnPlot"))
        self.horizontalLayout.addWidget(self.btnPlot)
        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setObjectName(_fromUtf8("status"))
        self.horizontalLayout.addWidget(self.status)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fileFrame = FileFrame(self.centralwidget)
        self.fileFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fileFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.fileFrame.setObjectName(_fromUtf8("fileFrame"))
        self.verticalLayout.addWidget(self.fileFrame)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 515, 392))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.beforeFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.beforeFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.beforeFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.beforeFrame.setObjectName(_fromUtf8("beforeFrame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.beforeFrame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.beforeFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.btnHideba = QtGui.QPushButton(self.beforeFrame)
        self.btnHideba.setCheckable(True)
        self.btnHideba.setChecked(True)
        self.btnHideba.setObjectName(_fromUtf8("btnHideba"))
        self.horizontalLayout_2.addWidget(self.btnHideba)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.widget = QtGui.QWidget(self.beforeFrame)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.beforeText = QtGui.QPlainTextEdit(self.widget)
        self.beforeText.setObjectName(_fromUtf8("beforeText"))
        self.verticalLayout_3.addWidget(self.beforeText)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.afterText = QtGui.QPlainTextEdit(self.widget)
        self.afterText.setObjectName(_fromUtf8("afterText"))
        self.verticalLayout_3.addWidget(self.afterText)
        self.verticalLayout_4.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.beforeFrame)
        self.topArea = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topArea.sizePolicy().hasHeightForWidth())
        self.topArea.setSizePolicy(sizePolicy)
        self.topArea.setObjectName(_fromUtf8("topArea"))
        self.verticalLayout_2.addWidget(self.topArea)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        SimWin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SimWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Simulation = QtGui.QMenu(self.menubar)
        self.menu_Simulation.setObjectName(_fromUtf8("menu_Simulation"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menu_Window = QtGui.QMenu(self.menubar)
        self.menu_Window.setObjectName(_fromUtf8("menu_Window"))
        SimWin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SimWin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SimWin.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(SimWin)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(SimWin)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(SimWin)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveAs = QtGui.QAction(SimWin)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionExit = QtGui.QAction(SimWin)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRun = QtGui.QAction(SimWin)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionAbort = QtGui.QAction(SimWin)
        self.actionAbort.setObjectName(_fromUtf8("actionAbort"))
        self.actionPlot = QtGui.QAction(SimWin)
        self.actionPlot.setObjectName(_fromUtf8("actionPlot"))
        self.actionAbout = QtGui.QAction(SimWin)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAboutQt = QtGui.QAction(SimWin)
        self.actionAboutQt.setObjectName(_fromUtf8("actionAboutQt"))
        self.actionLogWindow = QtGui.QAction(SimWin)
        self.actionLogWindow.setObjectName(_fromUtf8("actionLogWindow"))
        self.actionEditNet = QtGui.QAction(SimWin)
        self.actionEditNet.setObjectName(_fromUtf8("actionEditNet"))
        self.menu_File.addAction(self.actionNew)
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionSaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menu_Simulation.addAction(self.actionRun)
        self.menu_Simulation.addAction(self.actionAbort)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menu_Window.addAction(self.actionEditNet)
        self.menu_Window.addAction(self.actionPlot)
        self.menu_Window.addAction(self.actionLogWindow)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Simulation.menuAction())
        self.menubar.addAction(self.menu_Window.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(SimWin)
        QtCore.QObject.connect(self.btnHideba, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget.setVisible)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), SimWin.close)
        QtCore.QObject.connect(self.btnRun, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionRun.trigger)
        QtCore.QObject.connect(self.btnStop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionAbort.trigger)
        QtCore.QObject.connect(self.btnPlot, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionPlot.trigger)
        QtCore.QMetaObject.connectSlotsByName(SimWin)

    def retranslateUi(self, SimWin):
        SimWin.setWindowTitle(QtGui.QApplication.translate("SimWin", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSim.setText(QtGui.QApplication.translate("SimWin", "Add Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRun.setText(QtGui.QApplication.translate("SimWin", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStop.setText(QtGui.QApplication.translate("SimWin", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPlot.setText(QtGui.QApplication.translate("SimWin", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setText(QtGui.QApplication.translate("SimWin", "<Status>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SimWin", "Before/After each Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHideba.setText(QtGui.QApplication.translate("SimWin", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SimWin", "Before:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SimWin", "After", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("SimWin", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Simulation.setTitle(QtGui.QApplication.translate("SimWin", "&Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("SimWin", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Window.setTitle(QtGui.QApplication.translate("SimWin", "&Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("SimWin", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("SimWin", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("SimWin", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("SimWin", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("SimWin", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("SimWin", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("SimWin", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("SimWin", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("SimWin", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("SimWin", "&Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setShortcut(QtGui.QApplication.translate("SimWin", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbort.setText(QtGui.QApplication.translate("SimWin", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlot.setText(QtGui.QApplication.translate("SimWin", "&Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlot.setShortcut(QtGui.QApplication.translate("SimWin", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("SimWin", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setText(QtGui.QApplication.translate("SimWin", "aboutQt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogWindow.setText(QtGui.QApplication.translate("SimWin", "&Log Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditNet.setText(QtGui.QApplication.translate("SimWin", "&Edit Net/Schem.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditNet.setShortcut(QtGui.QApplication.translate("SimWin", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))

from .fileframe import FileFrame
from . import bench_rc
