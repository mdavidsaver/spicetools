# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import os, os.path, tempfile

from PyQt4 import QtCore, QtGui

from .ui_simmain import Ui_MainWindow

import dictmodel

_gnetlist = "gnetlist -g spice-sdb -O include_mode -O nomunge_mode -o %(net)s %(sch)s"

simtip = """tran Tstep Tstop [ Tstart [ Tmax ] ] [ UIC ]
dc Source-Name Vstart Vstop Vincr [ Source2 Vstart2 Vstop2 Vincr2 ]
ac ( DEC | OCT | LIN ) N Fstart Fstop
op
"""

simconfig = {
    'columns':[
        {'name':'label'},
        {'name':'Analysis', 'tip':simtip},
    ],
}
varconfig = {
    'columns':[
        {'name':'label'},
        {'name':'expression'},
    ]
}

class SimWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.netType.addItems(["Net list", "Schematic"])
        self.ui.netType.setCurrentIndex(1)

        F =self.fselect = QtGui.QFileDialog(self)
        F.setDirectory(os.getcwd())
        F.setFileMode(QtGui.QFileDialog.ExistingFile)
        F.setReadOnly(True)
        F.setNameFilters(["Nets/Schem. (*.net *.sch)","All files (*)"])

        app = QtGui.QApplication.instance()
        self.ui.actionQuit.triggered.connect(app.quit)
        
        self.ui.actionOpen.triggered.connect(F.show)

        self.ui.simBtn.clicked.connect(self.simulate)

        self.ui.addAnalysis.clicked.connect(self.ui.tblAnalysis.insertBlankRow)
        self.ui.delAnalysis.clicked.connect(self.ui.tblAnalysis.removeRows)

        self.ui.addCalc.clicked.connect(self.ui.tblCalc.insertBlankRow)
        self.ui.delCalc.clicked.connect(self.ui.tblCalc.removeRows)

        self.setWindowTitle('Spice Simulation Workbench')

        self.sims = dictmodel.DictTable(simconfig)
        self.vars = dictmodel.DictTable(varconfig)

        self.ui.tblAnalysis.setModel(self.sims)
        self.ui.tblCalc.setModel(self.vars)

        self.results = None
        self.tempdir = None
        self.proc = QtCore.QProcess()

        self.proc.readyReadStandardError.connect(self.simOutput)
        self.proc.readyReadStandardOutput.connect(self.simOutput)
        self.proc.finished.connect(self.simDone)

    def closeEvent(self, evt):
        if self.tempdir:
            self.removeTemp()
        evt.accept()

    def simOutput(self):
        self.proc.setReadChannel(self.proc.StandardError)
        err = self.proc.readAll()
        if err.size():
            print 'stderr',err
        self.proc.setReadChannel(self.proc.StandardOutput)
        out = self.proc.readAll()
        if out.size():
            print 'stderr',out

    def simDone(self, code, sts):
        print 'Simulation done', code, sts

    def simulate(self):
        self.tempdir = tempfile.mkdtemp()

        fname = self.fselect.selectedFiles()
        if len(fname)==0:
            print 'No file'
            return
        fname = str(fname[1])
        srcdir = os.path.abspath(os.path.dirname(fname))

        typeidx = self.ui.netType.currentIndex()
        assert typeidx==-1
        if typeidx==1:
            net = os.path.join(self.tempdir, 'generated.net')
            # must generate netlist...
            cmd = _gnetlist%{'sch':fname, 'net':str(net)}
            print 'Run:',cmd
            P = QtCore.QProcess(self)
            P.start(cmd)
            if not P.waitForFinished(2000):
                print 'gnetlist took too long...'
                P.kill()
                return
            elif P.exitCode()!=0:
                print 'gnetlist error',P.exitCode()
                return
            net = 'generated.net'
        else:
            net = os.path.basename(fname)

        script = os.path.join(self.tempdir, 'script.net')
        with open(script, 'w') as S:
            S.write("""* Generated circuit
.control
set sourcepath = ( "%(temp)s" "%(src)s" )
source %(net)s
echo "Net list loaded"
"""%{'temp':self.tempdir, 'src':srcdir, 'net':net})



    def plot(self):
        if not self.results:
            return

    def removeTemp(self):
        if not self.tempdir:
            return
        for path, dirs, files in os.walk(self.tempdir, topdown=False):
            for F in files:
                print 'remove file',os.path.join(path, F)
                os.remove(os.path.join(path, F))
            for D in dirs:
                print 'remove empty',os.path.join(path, D)
                os.rmdir(os.path.join(path, D))
        print 'remove top',self.tempdir
        os.rmdir(self.tempdir)
