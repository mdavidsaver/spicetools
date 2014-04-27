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
    @QtCore.pyqtSlot()
    def showLog(cls):
        if cls.instance is None:
            cls.instance = cls()
        cls.instance.show()

    def __init__(self):
        super(LogWin,self).__init__()
        self.setAttribute(QtCore.Qt.WA_QuitOnClose, False)

        self.ui = Ui_LogWin()
        self.ui.setupUi(self)

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
        evt.accept()

    @QtCore.pyqtSlot()
    def clear(self):
        self._Q = []
        self.write("clear")

    def write(self, msg):
        self._Q.append(msg.rstrip())
        self._Q = self._Q[-100:]

        if not self.timer:
            self.startTimer(100)
            self.timer = True

    def flush(self):
        pass

    def timerEvent(self, evt):
        self.timer = False
        self.killTimer(evt.timerId())
        evt.accept()

        self.ui.log.setPlainText('\n'.join(self._Q))

    def _saveLog(self, fname):
        with open(str(fname), 'w') as F:
            F.write('\n'.join(self._Q))