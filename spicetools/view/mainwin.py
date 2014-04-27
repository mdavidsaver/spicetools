# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import os, traceback

import numpy

from PyQt4 import (QtGui as gui, QtCore as core)

from .mainwin_ui import Ui_MainWindow
from ..io import loadspice

class ViewerWindow(gui.QMainWindow):
    def __init__(self):
        gui.QMainWindow.__init__(self)

        app = gui.QApplication.instance()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = core.QSettings("spicetools", "benchui")
        self.restoreGeometry(self.settings.value("viewerwindow/geometry").toByteArray())

        F =self.fselect = gui.QFileDialog(self)
        F.setDirectory(os.getcwd())
        F.setFileMode(gui.QFileDialog.ExistingFile)
        F.setReadOnly(True)

        self.ui.signals.itemSelectionChanged.connect(self.updateTraces)
        self.ui.xaxis.activated.connect(self.updateTraces)
        self.ui.ops.activated.connect(self.updateTraces)
        self.ui.sets.activated.connect(self.switchSet)

        self.ui.actionOpen.triggered.connect(F.show)
        self.ui.actionReload.triggered.connect(self.reloadFile)
        self.ui.actionClose.triggered.connect(self.closeFile)
        self.ui.actionCloneWindow.triggered.connect(self.newWin)

        F.fileSelected.connect(self.open)

        self.ui.actionAboutQt.triggered.connect(app.aboutQt)
        self.ui.actionAbout.triggered.connect(self.about)

        self.closeFile()

        self.saveSet = self.saveX = self.saveY = self.saveOp = None
        self.nodraw = False

    instances = set()

    def showEvent(self, evt):
        # keep visible windows from being GC'd
        self.instances.add(self)
        evt.accept()

    def closeEvent(self, evt):
        self.settings.setValue("viewerwindow/geometry", self.saveGeometry())
        self.settings.sync()
        evt.accept()
        self.instances.remove(self)

    @core.pyqtSlot(str)
    def open(self, fname):
        print 'Open file',fname

        fname = str(fname)
        try:
           fset = loadspice(fname)

        except Exception as E:
            gui.QMessageBox.critical(self, "File Error",
                                     "Failed to open '%s'\n%s"%(fname, E))
            traceback.print_exc()
            return

        self.loadData(fset)

    @core.pyqtSlot(object)
    def loadData(self, fset):
        self.saveOp = str(self.ui.ops.currentText()) or None
        self.saveSet = str(self.ui.sets.currentText()) or None
        self.saveX = str(self.ui.xaxis.currentText()) or None
        self.saveY = set([str(I.text()) for I in self.ui.signals.selectedItems()]) or None

        self.nodraw = True
        self.closeFile()
        self.fset = fset

        self.ui.sets.addItems(fset.keys())
        if self.saveSet:
            self.ui.sets.setCurrentIndex(self.ui.sets.findText(self.saveSet))
        if self.ui.sets.currentIndex()==-1:
            self.ui.sets.setCurrentIndex(0)
        self.nodraw = False

        self.switchSet()

        self.setWindowTitle('SpiceViewer - %s'%fset.name)
        self.ui.signals.setEnabled(True)
        self.ui.xaxis.setEnabled(True)
        self.ui.sets.setEnabled(True)

        self.updateTraces()

    @core.pyqtSlot()
    def reloadFile(self):
        if self.fset and self.fset.name:
            self.open(self.fset.name)

    @core.pyqtSlot()
    def closeFile(self):
        self.fset = None
        self.setWindowTitle('SpiceViewer')
        self.ui.signals.setEnabled(False)
        self.ui.xaxis.setEnabled(False)
        self.ui.sets.setEnabled(False)
        self.ui.signals.clear()
        self.ui.xaxis.clear()
        self.ui.sets.clear()
        self.ui.canvas.reset()

    @core.pyqtSlot()
    def switchSet(self):
        S = str(self.ui.sets.currentText())
        print 'switch to vector set',S
        if not S:
            return

        Vs = self.fset[S]
        defx = Vs.labels[0]

        if not self.saveX:
            self.saveX = str(self.ui.xaxis.currentText()) or None
        if not self.saveY:
            self.saveY = set([str(I.text()) for I in self.ui.signals.selectedItems()]) or None

        self.ui.signals.clear()
        self.ui.xaxis.clear()
        self.ui.ops.clear()

        self.ui.signals.addItems(Vs.keys())
        self.ui.xaxis.addItems(Vs.keys())

        newopts = Vs.ops.keys()
        newopts.sort()
        self.ui.ops.addItems(newopts)

        self.ui.xaxis.setCurrentIndex(self.ui.xaxis.findText(defx))

        self.nodraw = True

        if self.saveOp:
            self.ui.ops.setCurrentIndex(self.ui.ops.findText(self.saveOp))
        if self.ui.ops.currentIndex()==-1:
            self.ui.ops.setCurrentIndex(0)

        if self.saveX:
            self.ui.xaxis.setCurrentIndex(self.ui.xaxis.findText(self.saveX))
        if self.ui.xaxis.currentIndex()==-1:
            self.ui.xaxis.setCurrentIndex(self.ui.xaxis.findText(defx))
        if self.ui.xaxis.currentIndex()==-1:
            self.ui.xaxis.setCurrentIndex(0)

        if self.saveY:
            for n in range(self.ui.signals.count()):
                item = self.ui.signals.item(n)
                if str(item.text()) in self.saveY:
                    item.setSelected(True)

        self.nodraw = False

        self.updateTraces()

    @core.pyqtSlot()
    def updateTraces(self):
        if self.nodraw:
            return
        print 'update'
        op = str(self.ui.ops.currentText())
        S = str(self.ui.sets.currentText())
        X = str(self.ui.xaxis.currentText())
        items = [str(I.text()) for I in self.ui.signals.selectedItems()]

        if not op or not S or not X or len(items)==0:
            self.ui.canvas.reset()
            return

        Vs = self.fset[S]

        print 'Plot',S,X,items
        xdata = numpy.real(Vs[X])
        ydata = [Vs.value(n,op) for n in items]

        self.ui.canvas.plot(xdata, ydata, items)

        self.saveSet = self.saveX = self.saveY = self.saveOp = None

    @core.pyqtSlot()
    def newWin(self):
        W = ViewerWindow()
        W.loadData(self.fset)
        W.show()

    @core.pyqtSlot()
    def about(self):
        gui.QMessageBox.about(self, "About SpiceViewer",_about)


_about="""<h2>SpiceViewer</h2>
<p>ngspice output waveform viewer 1.0
</p>
<p>Extracts waveform data from ngspice binary and ascii format
data files.  Also the HDF5 files generated by spice2hdf.
</p>
<p>Copyright 2014, Michael Davidsaver &lt;mdavidsaver@gmail.com&gt;.
License GPL3+
</p>
"""
