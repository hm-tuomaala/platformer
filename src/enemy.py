from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt
import globals
import math


class Enemy(QGraphicsRectItem):
    def __init__(self, start_x, start_y, parent = None):
        QGraphicsRectItem.__init__(self, parent)
        self.x = start_x
        self.y = start_y
        self.vel_y = 0
        self.vel_x = 0
        self.setRect(self.x, self.y, 40, 40)
        self.setBrush(QBrush(Qt.green))
        self.can_move = True

    def set_enemy(self):
        self.setRect(self.x, self.y, 40, 40)

    def move(self):
        if self.can_move:
            self.vel_x = -2
        else:
            self.vel_x = 2

    def enemy_update(self, map):

        self.move()
        self.vel_y += globals.GRAVITY

        new_x = self.x + self.vel_x
        new_y = self.y + self.vel_y

        if self.vel_x <= 0:
            if map.map[math.floor(self.y/40)][math.floor(new_x/40)] == 1 or map.map[math.floor((self.y+38)/40)][math.floor(new_x/40)] == 1:
                new_x = math.floor(new_x/40)*40 + 40
                self.vel_x = 0
                self.can_move = False
        else:
            if map.map[math.floor(self.y/40)][math.floor((new_x+40)/40)] == 1 or map.map[math.floor((self.y+38)/40)][math.floor((new_x+40)/40)] == 1:
                new_x = math.floor(new_x/40)*40
                self.vel_x = 0
                self.can_move = True

        if self.vel_y > 0:
            if map.map[math.floor((new_y+40)/40)][math.floor(new_x/40)] == 1 or map.map[math.floor((new_y+40)/40)][math.floor((new_x+38)/40)] == 1:
                new_y = math.floor(new_y/40)*40
                self.vel_y = 0

        self.x = new_x
        self.y = new_y

        self.set_enemy()
