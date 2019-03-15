from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
PLAYER_SPEED            = 3   # pix/frame
FRAME_TIME_MS           = 16  # ms/frame
GRAVITY                 = 0.6

class Enemy(QGraphicsRectItem):
    def __init__(self, strat_x, parent = None):
        QGraphicsRectItem.__init__(self, parent)
        self.x = strat_x
        self.flag = True
        self.setRect(self.x, SCREEN_HEIGHT - 30, 30, 30)
        self.setBrush(QBrush(Qt.green))

    def set_enemy(self):
        self.setRect(self.x, SCREEN_HEIGHT - 30, 30, 30)

    def enemy_update(self):
        if self.flag:
            self.x -= 5
            self.set_enemy()
        elif not self.flag:
            self.x += 5
            self.set_enemy()

        if self.x <= 0:
            self.flag = False
        if self.x >= SCREEN_WIDTH - 30:
            self.flag = True
        #pass
