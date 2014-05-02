# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from PyQt4 import QtGui as gui

from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QTAgg as NavigationToolbar)
from matplotlib.figure import Figure, Axes

colors = [
    'r-',
    'b-',
    'k-',
    'g-',
    'r--',
    'b--',
    'k--',
    'g--',
]

class PlotArea(gui.QWidget):
    def __init__(self, parent=None):
        super(PlotArea, self).__init__(parent)

        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(True)

        layout = gui.QVBoxLayout(self)

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        # present values in self.fig.subplotpars.*
        self.fig.subplots_adjust(left=0.125,
                                 bottom=0.137,
                                 right=0.972,
                                 top=0.957)

    def reset(self):
        self.axes.clear()
        self.canvas.draw()

    def plot(self, X, Ys, labels):
        self.axes.clear()
        if len(Ys)==0:
            self.draw()
            return

        assert len(labels)==len(Ys)

        for i in range(len(Ys)):
            self.axes.plot(X, Ys[i], colors[i%len(colors)], label=labels[i])

        self.axes.legend(bbox_to_anchor=(0., -0.15, 1., .102), loc=3,
                         ncol=4, mode="expand", borderaxespad=0.)
        self.canvas.draw()
