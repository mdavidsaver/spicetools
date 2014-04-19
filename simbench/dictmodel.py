# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from copy import deepcopy

from PyQt4 import QtCore
from PyQt4.QtCore import Qt

exampleconfig = {
  'columns': [
      {'name':'col1', 'default':'', 'tip':'This is column 1'},
      {'name':'col2', 'default':'Hello'},
      {'name':'col3'},
  ],
}


class DictTable(QtCore.QAbstractTableModel):
    """A Tabular access to a list of dictionaries
    """

    def __init__(self, options, data = None, parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.conf = options
        # map of column # to dict key
        self.C2K = dict(enumerate([C['name'] for C in self.conf['columns']]))
        self.L = data or []

    def _newItem(self):
        "Build A new dictionary"
        return dict([(C['name'],deepcopy(C.get('default',None))) for C in self.conf['columns']])

    def _getItem(self, idx):
        R, C = idx.row(), idx.column()
        key = self.C2K[C]
        item = self.L[R]
        return item, key, R

    def rowCount(self, idx=QtCore.QModelIndex()):
        return len(self.L)

    def columnCount(self, idx=QtCore.QModelIndex()):
        return len(self.conf['columns'])

    def headerData(self, col, orient, role):
        #print 'headerData',col,orient,role
        if orient==Qt.Horizontal and role==Qt.DisplayRole:
            R = self.conf['columns'][col]['name']
            return R

    def flags(self, idx):
        flags = QtCore.QAbstractTableModel.flags(self, idx)
        return flags | Qt.ItemIsEditable

    def setData(self, idx, val, role):
        if role!=Qt.EditRole:
            return False
        item, key, row = self._getItem(idx)
        item[key] = str(val.toString())
        self.dataChanged.emit(idx, idx)
        #print 'set',row,key,'to',item[key]
        #print '  now',item
        return True

    def data(self, idx, role):
        if not idx.isValid():
            return
        elif role==Qt.ToolTipRole:
            return self.conf['columns'][idx.row()].get('tip', None)
        elif role not in [Qt.DisplayRole, Qt.EditRole]:
            return

        assert idx.isValid()
        item, key, row = self._getItem(idx)
        #print 'get',row,key,item[key]
        return item[key]

    def insertRows(self, row, cnt, idx=QtCore.QModelIndex()):
        #print 'insertRows',row,cnt
        self.beginInsertRows(QtCore.QModelIndex(), row, row+cnt-1)
        for n in range(cnt):
            self.L.insert(row, self._newItem())
        self.endInsertRows()
        return True

    def removeRows(self, row, cnt, idx=QtCore.QModelIndex()):
        #print 'removeRows',row,cnt
        self.beginRemoveRows(QtCore.QModelIndex(), row, row+cnt-1)
        for n in range(cnt):
            self.L.pop(row)
        self.endRemoveRows()
        return True

def test():
    import sys
    from PyQt4 import QtGui
    import editable
    app = QtGui.QApplication(sys.argv)
    mod = DictTable(exampleconfig)
    view = editable.EditTable()
    view.setSelectionMode(view.MultiSelection)
    view.setSelectionBehavior(view.SelectRows)
    view.setEditTriggers(view.DoubleClicked|view.AnyKeyPressed)

    view.setModel(mod)
    view.show()
    return app.exec_()

if __name__=='__main__':
    test()
