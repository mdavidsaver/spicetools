# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import os, os.path

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QStandardItem, QBrush

from .varedit import VarEdit

def iterRows(item):
    for n in range(item.rowCount()):
        yield item.child(n,0)

class VarNode(QStandardItem):
    itype = 'vars'
    def __init__(self):
        QStandardItem.__init__(self, "Expressions")
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)

class SimNode(QStandardItem):
    itype = 'sims'
    def __init__(self):
        QStandardItem.__init__(self, "Analyses")
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)

class PlotNode(QStandardItem):
    itype = 'plots'
    def __init__(self):
        QStandardItem.__init__(self, "Plots")
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)

class Project(QStandardItem):
    itype = 'project'
    def __init__(self):
        QStandardItem.__init__(self, "Project")
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.pfile, self.nfile = None, None

        self.vars = VarNode()
        self.sims = SimNode()

        self.insertRows(0, [self.vars, self.sims])

    def itervars(self):
        return iterRows(self.vars)
    def itersims(self):
        return iterRows(self.sims)

class Sim(QStandardItem):
    itype = 'sim'
    def __init__(self, name, line):
        QStandardItem.__init__(self)
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.name, self.line = name, line
        self.setText(name)

        self.vars = VarNode()
        self.plots = PlotNode()

        self.insertRows(0, [self.vars, self.plots])

    def itervars(self):
        return iterRows(self.vars)
    def iterplots(self):
        return iterRows(self.plots)

class Calc(QStandardItem):
    itype = 'sim'
    def __init__(self, name, expr):
        QStandardItem.__init__(self, name)
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.name, self.expr = name, expr
        self.win = VarEdit(self)

class Plot(object):
    itype = 'sim'
    def __init__(self, name):
        QStandardItem.__init__(self, name)
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.name = name
