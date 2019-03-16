from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
PLAYER_SPEED            = 3   # pix/frame
FRAME_TIME_MS           = 16  # ms/frame
GRAVITY                 = 0.6

class Platform(QGraphicsRectItem):
    def __init__(self, x, y, w, parent = None):
        QGraphicsRectItem.__init__(self, parent)
        self.x = x
        self.y = y
        self.width = w
        self.height = 10
        self.setRect(self.x, self.y, self.width, self.height)
        self.setBrush(QBrush(Qt.white))
