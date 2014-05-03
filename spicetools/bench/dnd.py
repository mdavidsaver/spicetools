# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

from PyQt4.QtGui import QDrag
from PyQt4.QtCore import Qt, QMimeData

class DragAndDropMixin(object):
    """Widget to Widget Drag and drop helper

    Implements minimum move distance to start a drag,
    as well as drop target validation based QWidget sub-class.
    """

    minDragDist = 10
    acceptableDrops = ()

    def mousePressEvent(self, evt):
        if evt.button()==Qt.LeftButton:
            self.__downPos = evt.pos()

    def mouseMoveEvent(self, evt):
        if not (evt.buttons()&Qt.LeftButton):
            return
        if (evt.pos()-self.__downPos).manhattanLength()<self.minDragDist:
            return

        D = QDrag(self)
        data = QMimeData()
        data.setData("application/x-internal", '')
        D.setMimeData(data)

        D.exec_(Qt.MoveAction)

    def canDrop(self, evt):
        if evt.source() in [self, None]:
            return False
        return isinstance(evt.source(), self.acceptableDrops)

    def dragEnterEvent(self, evt):
        if self.canDrop(evt):
            evt.acceptProposedAction()

    def dropEvent(self, evt):
        if self.canDrop(evt):
            evt.acceptProposedAction()
            print 'Drop',evt.source(),'onto',self
