from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt
import globals


class Enemy(QGraphicsRectItem):
    def __init__(self, start_x, dist, parent = None):
        QGraphicsRectItem.__init__(self, parent)
        self.x = start_x
        self.vasemmalle = True #determines direction of enemy
        self.setRect(self.x, globals.SCREEN_HEIGHT - 40, 40, 40)
        self.setBrush(QBrush(Qt.green))
        self.kuljettu = 0
        self.distance = dist

    def set_enemy(self):
        self.setRect(self.x, globals.SCREEN_HEIGHT - 40, 40, 40)

    def enemy_update(self):
        if self.vasemmalle:
            self.x -= 2
            self.kuljettu += 2
            self.set_enemy()
        else:
            self.x += 2
            self.kuljettu += 2
            self.set_enemy()
        if self.kuljettu >= self.distance:
            if self.vasemmalle:
                self.vasemmalle = False
            else:
                self.vasemmalle = True
            self.kuljettu = 0

        # if self.flag:
        #     self.x -= 2
        #     self.set_enemy()
        # elif not self.flag:
        #     self.x += 2
        #     self.set_enemy()
        #
        # if self.x <= 0:
        #     self.flag = False
        # if self.x >= globals.SCREEN_WIDTH - 30:
        #     self.flag = True
