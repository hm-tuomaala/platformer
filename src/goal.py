from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem


class Goal(QGraphicsPixmapItem):

    def __init__(self, x, y, parent = None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.x = x
        self.y = y
        self.counter = 0
        self.victory = False
        self.animation = [QPixmap("static/flag1"), QPixmap("static/flag2"),
                          QPixmap("static/flag3"), QPixmap("static/flag4"),
                          QPixmap("static/flag5"), QPixmap("static/flag6"),
                          QPixmap("static/flag7")]

        self.setPixmap(self.animation[0])
        self.setPos(self.x, self.y)
