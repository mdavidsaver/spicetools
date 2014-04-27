# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
_log=logging.getLogger(__name__)

import sys, os, os.path, tempfile, json

from PyQt4 import QtCore

#from spiceviewer.spiceio import readhdf5

IDLE = 0
START = 1
RUN = 2
ERR = 3

STATES = {
    0:'Idle',
    1:'Start',
    2:'Run',
    3:'Error',
}

class SpiceRunner(QtCore.QObject):
    stateChanged = QtCore.pyqtSignal(str)
    done = QtCore.pyqtSignal(object)
    msg = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(SpiceRunner, self).__init__(parent)

        self._state, self._D = IDLE, None

        self.runner = QtCore.QProcess(self) # runs gnetlist
        
        self.runner.setProcessChannelMode(self.runner.MergedChannels)

        self.runner.started.connect(self._started)
        self.runner.finished.connect(self._finished)
        self.runner.error.connect(self._error)
        self.runner.readyRead.connect(self._read)

        self.tempprj = None

    def state(self):
        return STATES.get(self._state, 'Invalid')

    state = QtCore.pyqtProperty(str, state, notify=stateChanged)

    def _setState(self, S):
        self._state = S
        self.stateChanged.emit(self.state)

    @QtCore.pyqtSlot()
    def abort(self):
        self.msg.emit("Aborting")

        self.runner.kill()

        if self.tempprj:
            os.remove(self.tempprj)
            self.tempprj = None

        self.done.emit(None)
        self._setState(IDLE)

    @QtCore.pyqtSlot(object)
    def startSim(self, D):
        self.abort()
        try:
            FD, self.tempprj = tempfile.mkstemp()
            FD = os.fdopen(FD, 'w')
            json.dump(D, FD)

            pfileroot = os.path.splitext(D['projectfile'])[0]

            self.h5file = '%s.h5'%pfileroot
            args = ['-m','spicetools.sim','-v','--time',
                    self.tempprj, self.h5file]

            _log.debug("In %s", D['projectdir'])
            _log.debug("Running: %s %s", sys.executable, args)

            self.runner.setWorkingDirectory(D['projectdir'])
            self.runner.start(sys.executable, args)

            self._setState(START)
        except:
            self._setState(ERR)
            _log.exception("startSim failed")

    def _started(self):
        _log.debug("Process started")
        self._setState(RUN)

    def _finished(self, code, status):
        _log.debug("Process finished: %s %s",code,status)
        if code or status:
            self._setState(ERR)
        else:
            self._state = IDLE
            self.stateChanged.emit(STATES[IDLE])
            self.done.emit(self.h5file)

    def _error(self, err):
        _log.error("Process error: %s", err)
        self._setState(ERR)

    def _read(self):
        msg = self.runner.readAll()
        _log.debug("Process Read: %s", msg)
        self.msg.emit(QtCore.QString(msg))
