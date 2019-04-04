from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt
import globals

class Platform(QGraphicsRectItem):
    def __init__(self, x, y, parent = None):
        QGraphicsRectItem.__init__(self, parent)
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.setRect(self.x, self.y, self.width, self.height)
        self.setBrush(QBrush(Qt.white))
