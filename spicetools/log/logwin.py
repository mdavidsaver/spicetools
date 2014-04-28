# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
# We don't log to avoid loops
#_log=logging.getLogger(__name__)

import os

from PyQt4 import QtCore, QtGui

from .logwin_ui import Ui_LogWin
            

class LogWin(QtGui.QMainWindow):
    instance = None

    @classmethod
    def createLog(cls):
        if cls.instance is None:
            cls.instance = cls()

    @classmethod
    @QtCore.pyqtSlot()
    def showLog(cls):
        cls.createLog()
        cls.instance.show()

    @classmethod
    def visibleLog(cls):
        return cls.instance is not None and cls.instance.isVisible()

    def __init__(self):
        super(LogWin,self).__init__()
        self.setAttribute(QtCore.Qt.WA_QuitOnClose, False)

        self.ui = Ui_LogWin()
        self.ui.setupUi(self)

        self.ui.log.setMaximumBlockCount(200)
        self.ui.log.setCenterOnScroll(True)

        self.settings = QtCore.QSettings("spicetools", "benchui")
        self.restoreGeometry(self.settings.value("logwindow/geometry").toByteArray())

        self.save = QtGui.QFileDialog(self,
                         'Save current log contents',
                         os.getcwd(),
                         'Log file (*.log *.txt);;All Files (*)'
                         )
        self.save.setDefaultSuffix('.log')
        self.save.setAcceptMode(self.save.AcceptSave)

        self.ui.actionClear.triggered.connect(self.clear)

        self.ui.actionSaveAs.triggered.connect(self.save.show)
        self.save.fileSelected.connect(self._saveLog)

        self._Q = []
        self._H = logging.StreamHandler(self)
        self._H.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
        root = logging.getLogger()
        root.addHandler(self._H)
        self.timer = False

    def closeEvent(self, evt):
        root = logging.getLogger()
        root.removeHandler(self._H)
        self.instance = None
        self.settings.setValue("logwindow/geometry", self.saveGeometry())
        self.settings.sync()
        evt.accept()

    @QtCore.pyqtSlot()
    def clear(self):
        self._Q = []
        self.ui.log.setPlainText('')
        self.write("clear")

    def write(self, msg):
        if len(self._Q)>100:
            return # overflow...
        self._Q.append(msg.rstrip())

        if not self.timer:
            self.startTimer(100)
            self.timer = True

    def flush(self):
        pass

    def timerEvent(self, evt):
        self.timer = False
        self.killTimer(evt.timerId())
        evt.accept()

        for msg in self._Q:
            self.ui.log.appendPlainText(msg)

    def _saveLog(self, fname):
        with open(str(fname), 'w') as F:
            F.write(self.ui.log.toPlainText())
