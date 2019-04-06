from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsPixmapItem
from PyQt5.QtGui import QBrush, QPixmap
from PyQt5.QtCore import Qt
import globals

class Platform(QGraphicsPixmapItem):
    def __init__(self, x, y, val, parent = None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.x = x
        self.y = y
        # self.width = 40
        # self.height = 40
        # self.setRect(self.x, self.y, self.width, self.height)
        if val == 1:
            self.setPixmap(QPixmap("static/ground.png"))
            self.setPos(self.x, self.y)
        elif val == 2:
            self.setPixmap(QPixmap("static/water.png"))
            self.setPos(self.x, self.y)
        elif val == 3:
            self.setPixmap(QPixmap("static/box.png"))
            self.setPos(self.x, self.y)
        elif val == 4:
            self.setPixmap(QPixmap("static/tube_top.png"))
            self.setPos(self.x-5, self.y)
        elif val == 5:
            self.setPixmap(QPixmap("static/tube.png"))
            self.setPos(self.x, self.y)
        elif val == 6:
            self.setPixmap(QPixmap("static/tile1.png"))
            self.setPos(self.x, self.y)
