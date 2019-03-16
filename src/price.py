from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt


class Price(QGraphicsRectItem):

    def __init__(self, x, y, parent = None):
        QGraphicsRectItem.__init__(self, parent)
        self.x = x
        self.y = y
        self.w = 10
        self.h = 10
        self.setRect(self.x, self.y, self.w, self.h)
        self.setBrush(QBrush(Qt.red))
        self.available = True
        self.deleted = False

    def price_update(self):
        if not self.available:
            return True
