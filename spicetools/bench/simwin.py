# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
_log=logging.getLogger(__name__)

import os, os.path

import json, re

from PyQt4 import QtCore, QtGui

from .simwin_ui import Ui_SimWin
from .analysis import Analysis
from .spiceexec import SpiceRunner
from ..log.logwin import LogWin

from ..view.mainwin import ViewerWindow
from ..conf import loadConfig

# match (to remove) EOL whitespace
_trailing_space = re.compile(r'([ \t]+)$', re.MULTILINE)

class SimWin(QtGui.QMainWindow):
    requestStart = QtCore.pyqtSignal(object)

    def __init__(self):
        super(SimWin, self).__init__()
        
        self.ui = Ui_SimWin()
        self.ui.setupUi(self)

        self.log = LogWin()

        self.settings = QtCore.QSettings("spicetools", "benchui")
        self.restoreGeometry(self.settings.value("mainwindow/geometry").toByteArray())

        QtGui.QVBoxLayout(self.ui.topArea)
        self.ui.topArea.layout().insertStretch(1)

        self.sim = SpiceRunner(self)

        self.ui.actionNew.triggered.connect(self.clear)
        self.ui.actionOpen.triggered.connect(self._showOpen)
        self.ui.actionSave.triggered.connect(self._doSave)
        self.ui.actionSaveAs.triggered.connect(self._showSaveAs)
        self.ui.actionRun.triggered.connect(self.startSim)
        self.ui.actionAbort.triggered.connect(self.sim.abort)
        self.ui.actionPlot.triggered.connect(self._showPlot)
        self.ui.actionEditNet.triggered.connect(self._editNet)

        self.ui.btnSim.clicked.connect(self.addSim)

        self.requestStart.connect(self.sim.startSim)
        self.requestStart.connect(self.log.clear)
        self.sim.done.connect(self.simDone)
        self.sim.stateChanged.connect(self.ui.status.setText)

        self.ui.actionLogWindow.triggered.connect(self.log.show)
        self.log.setVisible(self.settings.value("mainwindow/showlog", False).toBool())

        self.ui.actionAboutQt.triggered.connect(QtGui.QApplication.instance().aboutQt)
        self.ui.actionAbout.triggered.connect(self.about)

        self.ui.status.setText(self.sim.state)

        self.dia = QtGui.QFileDialog(self, "Select Spice Project",
                                     os.getcwd(),
                                     "Net/Schem. (*.sprj);;All (*)")
        self.dia.setDefaultSuffix("sprj")        

        self.clear()

    def _updateFile(self, fname):
        self.fname = fname and str(fname)
        if fname:
            self.dia.selectFile(fname)
            F = self.dia.selectedFiles()
            fname = str(F[0]) if len(F)>0 else None
        if fname:
            fname = os.path.relpath(fname)
            self.setWindowTitle("Spice Bench - %s"%fname)
        else:
            self.setWindowTitle("Spice Bench")

    def closeEvent(self, evt):
        self.ui.actionAbort.trigger()
        self.settings.setValue("mainwindow/geometry", self.saveGeometry())
        self.settings.setValue("mainwindow/showlog", self.log.isVisible())
        self.log.sync()
        self.settings.sync()
        evt.accept()

    @QtCore.pyqtSlot()
    def startSim(self):
        _log.info('Start sim')
        D = self.todict()
        # Expand paths fully
        D['projectfile'] = os.path.abspath(self.fname or 'unsaved.proj')
        D['projectdir'] = os.path.dirname(D['projectfile'])
        if not os.path.isabs(D['net']['filename']):
            D['net']['filename'] = os.path.join(D['projectdir'],D['net']['filename'])
        _log.debug('Start sim with %s',D)
        self.requestStart.emit(D)

    @QtCore.pyqtSlot(object)
    def simDone(self, results):
        _log.debug('Sim done with %s',results)
        self.h5file = results
        for I in ViewerWindow.instances:
            I.reloadFile()

    def _showPlot(self):
        if self.h5file is None:
            return
        W = ViewerWindow()
        W.open(self.h5file)
        W.show()

    def addSim(self):
        A = Analysis(self.ui.topArea)
        A._level = 0
        self.ui.topArea.layout().insertWidget(0,A)

    def _editNet(self):
        if not self.ui.fileFrame.file:
            return
        fname = os.path.join(os.path.dirname(os.path.join(os.getcwd(),
                                                          str(self.fname or ''))),
                             str(self.ui.fileFrame.file))
        if not os.path.isfile(fname):
            return

        D = loadConfig(section='simbench')
        if self.ui.fileFrame.type:
            cmd = D['gschem.cmd']
        else:
            cmd = D['editor.cmd']

        cmd = cmd%{'file':fname}

        _log.debug("Starting: %s", cmd)

        if not QtCore.QProcess.startDetached(cmd):
            _log.error("Failed to start: %s", cmd)

    @QtCore.pyqtSlot()
    def clear(self):
        L = self.ui.topArea.layout()
        for C in self.ui.topArea.children():
            if C is L:
                continue
            C.deleteLater()

        self.ui.fileFrame.clear()

        self._updateFile(None)
        self.h5file = None
        _log.info("Clear bench")

    @QtCore.pyqtSlot()
    def _showOpen(self):
        self.dia.setFileMode(self.dia.ExistingFile)
        self.dia.setAcceptMode(self.dia.AcceptOpen)
        R = self.dia.exec_()
        F = self.dia.selectedFiles()
        if not R or len(F)==0:
            return
        self.open(str(F[0]))

    @QtCore.pyqtSlot()
    def _showSaveAs(self, _recurse=False):
        self.dia.setFileMode(self.dia.AnyFile)
        self.dia.setAcceptMode(self.dia.AcceptSave)
        R = self.dia.exec_()
        F = self.dia.selectedFiles()
        if not R or len(F)==0 or not F[0]:
            return
        F = str(F[0])
        if _recurse:
            return F

        self._doSave(F, _recurse=True)

        self._updateFile(F)

    @QtCore.pyqtSlot()
    def _doSave(self, fname=None, _recurse=False):
        if fname is None:
            fname = self.fname
        if fname is None:
            if not _recurse:
                fname = self._showSaveAs(_recurse=True)
        if fname is None:
            return
        elif not _recurse:
            self._updateFile(fname)

        self.save(fname)

    @QtCore.pyqtSlot(str)
    def open(self, F):
        F = str(F)
        _log.info('open: "%s"',F)
        with open(F,'r') as FP:
            D = json.load(FP)

        # validate
        if not isinstance(D, dict) or 'net' not in D or 'version' not in D:
            raise ValueError('Invalid json contents')
        elif D['version'] not in [1,2]:
            raise ValueError('Unsupported version: %s'%D['version'])

        try:
            self.clear()

            self.fromdict(D)

            self._updateFile(F)
        except:
            self.clear()
            raise

    @QtCore.pyqtSlot(str)
    def save(self, F):
        F = str(F)
        F = os.path.abspath(F)
        _log.info('save: "%s"',F)

        D = self.todict()

        if os.path.isabs(D['net']['filename']):
            # fix up net/schem filename to be relative to project file
            _log.debug("Input netfile: %s", D['net']['filename'])
            D['net']['filename'] = os.path.relpath(D['net']['filename'],
                                                   os.path.dirname(F))
            _log.debug("Output netfile: %s", D['net']['filename'])

        S = _trailing_space.sub('', json.dumps(D, indent=2))

        with open(F,'w') as FP:
            FP.write(S)
            FP.write('\n')

    def fromdict(self, D):
        from ..compat import updateDict
        D = updateDict(D)

        N = D['net']
        self.ui.fileFrame.file = N['filename']
        self.ui.fileFrame.type = N['schem']

        sims = D.get('sims',[])
        
        self.ui.beforeText.setPlainText(D.get('before',''))
        self.ui.afterText.setPlainText(D.get('after',''))

        L = self.ui.topArea.layout()

        for S in sims:
            A = Analysis(self.ui.topArea)
            A._level = 0
            A.setName(S['name'])
            A.setBefore(S['before'])
            A.setSim(S['line'])
            A.setAfter(S['after'])
            L.insertWidget(0, A)

    def todict(self):
        result = {'version':2,
             'net':{'filename':str(self.ui.fileFrame.file),
                    'schem':self.ui.fileFrame.type}}

        result['before'] = str(self.ui.beforeText.toPlainText())
        result['after'] = str(self.ui.afterText.toPlainText())

        sims = result['sims'] = []

        for C in self.ui.topArea.children():

            if isinstance(C, Analysis):
                S = {'name':str(C.name()), 'line':str(C.sim()),
                     'before':str(C.before()), 'after':str(C.after())}

                # save if any string is not empty
                if map(len, S.itervalues()) > 0:
                    sims.append(S)

        return result

    @QtCore.pyqtSlot()
    def about(self):
        QtGui.QMessageBox.about(self, "About SpiceBench",_about)


_about="""<h2>SpiceBench</h2>
<p>ngspice simulation controller 1.0
</p>
<p>Names a netlist or gschem file and lists analyses
which will be preformed on it.
</p>
<p>Copyright 2014, Michael Davidsaver &lt;mdavidsaver@gmail.com&gt;.
License GPL3+
</p>
"""
