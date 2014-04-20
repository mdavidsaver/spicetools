# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import os, os.path

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QStandardItem, QBrush

from .varedit import VarEdit
from .projectedit import ProjEdit
from .simedit import SimEdit

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

class Project(QStandardItem):
    itype = 'project'
    def __init__(self):
        QStandardItem.__init__(self, "Project")
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.fname, self.genNet = None, False

        self.vars = VarNode()
        self.sims = SimNode()
        self.win = ProjEdit(self)

        self.insertRows(0, [self.vars, self.sims])

    def itervars(self):
        return iterRows(self.vars)
    def itersims(self):
        return iterRows(self.sims)

class Sim(QStandardItem):
    itype = 'sim'
    def __init__(self):
        self.name, self.line = "<unnamed>", ""
        QStandardItem.__init__(self, self.name)
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)

        self.vars = VarNode()
        self.win = SimEdit(self)

        self.insertRows(0, [self.vars])

    def itervars(self):
        return iterRows(self.vars)
    def iterplots(self):
        return iterRows(self.plots)

class Calc(QStandardItem):
    itype = 'calc'
    def __init__(self):
        self.name, self.expr = "<unnamed>", ""
        QStandardItem.__init__(self, self.name)
        self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        self.win = VarEdit(self)
