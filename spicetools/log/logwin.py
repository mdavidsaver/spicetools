# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
# We don't log to avoid loops
#_log=logging.getLogger(__name__)

import os, traceback, re

from PyQt4 import QtCore, QtGui

from .logwin_ui import Ui_LogWin

_error = re.compile('\s*error.*', re.IGNORECASE)

class ErrorHighlight(QtGui.QSyntaxHighlighter):
    _formaters = [
        ('Process Read:', {'setFontWeight':QtGui.QFont.Bold}),
        ('error.*', {'setFontWeight':QtGui.QFont.Bold,
                     'setForeground':QtCore.Qt.red}),
    ]
    def __init__(self, *args):
        super(ErrorHighlight, self).__init__(*args)

        self.formaters = []
        for pat, As in self._formaters:
            R = QtCore.QRegExp(pat)
            R.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            fmt = QtGui.QTextCharFormat()
            for K,V in As.iteritems():
                F = getattr(fmt, K)
                F(V)
            self.formaters.append((R,fmt))

    def highlightBlock(self, S):
        try:
            for R, F in self.formaters:
                idx = R.indexIn(S)
                while idx>=0:
                    mlen = R.matchedLength()
                    assert mlen>0,'oops %s'%mlen
                    self.setFormat(idx, mlen, F)
                    idx = R.indexIn(S, idx+mlen)
        except:
            # trap exceptions here to prevent recursion in logging
            traceback.print_exc()
            print 'Error highlighting',S

class LogWin(QtGui.QMainWindow):
    def __init__(self):
        super(LogWin,self).__init__()
        self.setAttribute(QtCore.Qt.WA_QuitOnClose, False)

        self.ui = Ui_LogWin()
        self.ui.setupUi(self)

        doc = self.ui.log.document()
        doc.setMaximumBlockCount(1000)

        self._H = ErrorHighlight(doc)

        self._C = QtGui.QTextCursor(doc)

        self.settings = QtCore.QSettings("spicetools", "benchui")
        self.restoreGeometry(self.settings.value("logwindow/geometry").toByteArray())
        self.ui.autoClr.setChecked(self.settings.value("logwindow/autoclear").toBool())

        self.save = QtGui.QFileDialog(self,
                         'Save current log contents',
                         os.getcwd(),
                         'Log file (*.log *.txt);;All Files (*)'
                         )
        self.save.setDefaultSuffix('.log')
        self.save.setAcceptMode(self.save.AcceptSave)

        self.ui.actionClear.triggered.connect(self._real_clear)

        self.ui.actionSaveAs.triggered.connect(self.save.show)
        self.save.fileSelected.connect(self._saveLog)

        self._Q = []
        self._H = logging.StreamHandler(self)
        self._H.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
        root = logging.getLogger()
        root.addHandler(self._H)
        self.timer = False

        self._errors = 0

    def sync(self):
        self.settings.setValue("logwindow/geometry", self.saveGeometry())
        self.settings.setValue("logwindow/autoclear", self.ui.autoClr.isChecked())

    def closeEvent(self, evt):
        root = logging.getLogger()
        root.removeHandler(self._H)
        evt.accept()

    def clear(self):
        if self.ui.autoClr.isChecked():
            self._real_clear()

    def _real_clear(self):
        self._Q = []
        self.ui.log.setPlainText('')
        self.write("clear")
        self._errors = 0
        self.ui.errCnt.setText('0')

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
        try:
            Q, self._Q = self._Q, []

            self.timer = False
            self.killTimer(evt.timerId())

            # break multi-line log messages into individual lines
            L = []
            for q in map(str.splitlines, Q):
                L.extend(q)

            self._C.beginEditBlock()
            self._C.clearSelection()
            for msg in L:
                if _error.match(msg):
                    self._errors += 1
                self._C.insertText(msg+'\n')
            self._C.endEditBlock()
            self.ui.log.ensureCursorVisible()

            self.ui.errCnt.setText(str(self._errors))

            evt.accept()
        except:
            # trap exceptions here to prevent recursion in logging
            traceback.print_exc()
            print 'Error updating log'

    def _saveLog(self, fname):
        with open(str(fname), 'w') as F:
            F.write(self.ui.log.toPlainText())
