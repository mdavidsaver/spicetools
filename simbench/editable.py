# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details

An ediTable Table
"""

from PyQt4 import QtCore, QtGui

class EditTable(QtGui.QTableView):
    """A QTableView with helpers to insert and remove rows
    """

    @QtCore.pyqtSlot()
    def insertBlankRow(self):
        """Insert a blank row before the current selection,
        or at the end if empty.
        """
        print 'insert',self
        M = self.model()
        idx = self.currentIndex()
        if idx.isValid():
            row = idx.row()
        else:
            row = M.rowCount()
            
        M.insertRow(row, QtCore.QModelIndex())

    @QtCore.pyqtSlot()
    def removeRows(self):
        """Remove all rows with at least one element selected
        """
        SM = self.selectionModel()
        # Make a set to remove possible duplication
        # caused by item selection mode
        rows = set([R.row() for R in SM.selectedRows(0)])
        rows = list(rows)
        rows.reverse() # delete from end to beginning
        print 'Remove rows',rows
        
        M = self.model()
        for R in rows:
            M.removeRow(R, QtCore.QModelIndex())
