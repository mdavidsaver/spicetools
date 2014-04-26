# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
_log=logging.getLogger(__name__)

import os.path

from PyQt4 import QtCore

from .util import TempDir

from spiceviewer.spiceio import readhdf5

IDLE = 0 # Waiting for start
TONET = 1 # Waiting for schematic to netlist conversion
SIM = 2 # Waiting for simulation to complete
ERR = 3

STATES = {
    0:'Idle',
    1:'To Net',
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

        self.netter = QtCore.QProcess(self) # runs gnetlist
        self.simmer = QtCore.QProcess(self) # runs spice

        self.netter.finished.connect(self.netDone)
        self.simmer.finished.connect(self.spiceDone)

        self.tdir = TempDir()

    def state(self):
        return STATES.get(self._state, 'Invalid')

    state = QtCore.pyqtProperty(str, state, notify=stateChanged)

    def _setState(self, S):
        self._state = S
        self.stateChanged.emit(self.state)

    @QtCore.pyqtSlot()
    def abort(self):
        self.msg.emit("Aborting")

        if self.netter.state()!=self.netter.NotRunning:
            self.netter.kill()
        if self.simmer.state()!=self.simmer.NotRunning:
            self.simmer.kill()

        self.done.emit(None)
        self._setState(IDLE)

    @QtCore.pyqtSlot(object, object)
    def startSim(self, D, conf):
        self.abort()
        try:
            self.cmd, self.conf = D, conf
            if D['net']['schem']:
                _log.info("Need to generate schemtic from %s",D['net']['filename'])
                self._genNet()
            else:
                self.netfile = D['net']['filename']
                self._startSpice()
        except:
            self._setState(ERR)
            _log.exception("startSim failed")

    def _genNet(self):
        self.netfile = 'generated.net'
        A = {
            'gnetlist':self.conf['gnetlist'],
            'net':self.tdir.join(self.netfile),
            'sch':self.cmd['net']['filename'],
        }
        cmd = self.conf['gnetlist.cmd']%A

        _log.debug("In: %s",os.path.dirname(A['sch']))
        _log.debug("Running: '%s'", cmd)

        self.netter.setWorkingDirectory(os.path.dirname(A['sch']))
        self.netter.start(cmd)
        if not self.netter.waitForStarted(2000):
            self._setState(ERR)
            _log.error("gnetlist not started: %s", self.netter.error())
            self.netter.kill()
        else:
            self._setState(TONET)

    def netDone(self, code, sts):
        if code or sts:
            _log.error("Generated net %s %s",code,sts)
            _log.error("stdout: %s",self.netter.readAllStandardOutput())
            _log.error("stderr: %s",self.netter.readAllStandardError())
            self._setState(ERR)
            return

        try:
            if _log.isEnabledFor(logging.DEBUG):
                with open(self.tdir.join(self.netfile), 'r') as F:
                    for L in F.readlines():
                        _log.debug(L[:-1])

            self._startSpice()
        except:
            _log.exception("netDone failed")

    def _startSpice(self):
        _log.info("Starting spice")
        A = {
            'spice':self.conf['spice'],
            'deck':self.tdir.join('generated.cmd'),
        }

        cmd = self.conf['spice.cmd']%A

        _log.debug("In: %s",self.tdir.dirname)
        _log.debug("Running: '%s'", cmd)

        self.simmer.setWorkingDirectory(self.tdir.dirname)

        with open(A['deck'], 'w') as FP:
            self._generateScript(FP)

        self.simmer.start(cmd)
        if not self.simmer.waitForStarted(2000):
            self._setState(ERR)
            _log.error("spice not started: %s", self.simmer.error())
            self.simmer.kill()
        else:
            self._setState(SIM)

    def spiceDone(self, code, sts):
        if code or sts:
            _log.error("Generated net %s %s",code,sts)
            _log.error("stdout: %s",self.netter.readAllStandardOutput())
            _log.error("stderr: %s",self.netter.readAllStandardError())
            self._setState(ERR)
            return

        try:
            data = readhdf5(self.tdir.join('output.h5'))
            self._state = IDLE
            self.stateChanged.emit(STATES[IDLE])
            self.done.emit(data)

        except:
            _log.exception("netDone failed")

    def generateScript(self, FP):
        """Generate spice command script
        """

        FP.write(_script_header%{
            'netfile':os.path.basename(self.netfile),
            'netdir':os.path.dirname(self.netfile),
            'workdir':self.tdir.dirname,
        })

        topvars = dict([(V.name,V.expr) for V in self.cmd.get('vars',[])])

        for S in self.cmd['sims']:
            FP.write(_script_sim%{'name':S.name, 'line':S.line})

            locvars = dict([(V.name,V.expr) for V in S.get('vars',[])])

            Vars = topvars.copy()
            Vars.update(locvars)

            for K,V in Vars.iteritems():
                FP.write('let %s = %s'%(K,V))

            FP.write('write %s.raw', S.name)

        FP.write(_script_end)

_script_header = """* %(netdir)s/%(netfile)s
.control
set filetype = binary
set sourcepath = ( "%(workdir)s" "%(netdir)s" )
echo "%%% Loading Netlist"
source %(netfile)s
echo "%%% Loaded Netlist"
"""

_script_sim = """echo "Analysis %(name)s
%(line)s
"""

_script_end = """echo "%%% Done"
quit
.endc
.end
"""
