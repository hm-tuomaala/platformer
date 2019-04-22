from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsPixmapItem
from PyQt5.QtGui import QBrush, QPixmap
from PyQt5.QtCore import Qt


class Price(QGraphicsPixmapItem):

    def __init__(self, x, y, parent = None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.x = x
        self.y = y

        self.setPixmap(QPixmap("static/price.png"))
        self.setPos(self.x, self.y)

        self.available = True
        self.deleted = False

    def price_update(self):
        if not self.available:
            return True
