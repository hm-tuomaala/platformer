from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsPixmapItem
from PyQt5.QtGui import QBrush, QPixmap
from PyQt5.QtCore import Qt
import globals
import math




class Player(QGraphicsPixmapItem):
    def __init__(self, parent = None):
        #QGraphicsRectItem.__init__(self,parent)
        QGraphicsPixmapItem.__init__(self, parent)
        self.x = 100
        self.y = 100
        self.vel_x = 0
        self.vel_y = 0

        self.setPixmap(QPixmap("static/kario_right.png"))
        self.setPos(self.x, self.y)

        #self.setRect(self.x, self.y, 40, 40)
        #self.setBrush(QBrush(Qt.white))
        self.lift = -17
        self.can_jump = False
        self.points = 0
        self.alive = True

    def set_player(self, x, y):
        #self.setRect(x, y, 40, 40)
        self.setPos(x, y)


    def move(self, keys_pressed):
        if Qt.Key_Left in keys_pressed:
            self.vel_x = -globals.PLAYER_SPEED
            self.setPixmap(QPixmap("static/kario_left.png"))
        if Qt.Key_Right in keys_pressed:
            self.vel_x = globals.PLAYER_SPEED
            self.setPixmap(QPixmap("static/kario_right.png"))
        if Qt.Key_Space in keys_pressed:
            keys_pressed.remove(Qt.Key_Space)
            if self.vel_y == 0 and self.can_jump:
                self.vel_y = self.lift
                self.can_jump = False


    def player_update(self, keys_pressed, enemy, timer, prices, map):

        self.move(keys_pressed)

        # Painovoima
        self.vel_y += globals.GRAVITY

        # if self.vel_x > 10:
        #     self.vel_x = 10
        # if self.vel_x < -10:
        #     self.vel_x = -10
        # if self.vel_y > 100:
        #     self.vel_y = 100
        # if self.vel_y < -100:
        #     self.vel_y = -100


        new_x = self.x + self.vel_x
        new_y = self.y + self.vel_y


        # Tormayksen tarkistus
        if self.vel_x <= 0:
            if map.map[math.floor(self.y/40)][math.floor(new_x/40)] != 0 or map.map[math.floor((self.y+36)/40)][math.floor(new_x/40)] != 0:
                new_x = math.floor(new_x/40)*40 + 40
                self.vel_x = 0
        else:
            if map.map[math.floor(self.y/40)][math.floor((new_x+40)/40)] != 0 or map.map[math.floor((self.y+36)/40)][math.floor((new_x+40)/40)] != 0:
                new_x = math.floor(new_x/40)*40
                self.vel_x = 0

        if self.vel_y <= 0:
            if map.map[math.floor(new_y/40)][math.floor(new_x/40)] != 0 or map.map[math.floor((new_y)/40)][math.floor((new_x+36)/40)] != 0:
                new_y = math.floor(new_y/40)*40 + 40
                self.vel_y = 0
        else:
            if map.map[math.floor((new_y+40)/40)][math.floor(new_x/40)] != 0 or map.map[math.floor((new_y+40)/40)][math.floor((new_x+36)/40)] != 0:
                new_y = math.floor(new_y/40)*40
                self.vel_y = 0
                self.can_jump = True

        self.x = new_x
        self.y = new_y

        self.set_player(self.x, self.y)

        self.vel_x = 0


        # Tarkastetaan vihollisen sijainti
        if self.x + 40 > enemy.x and self.x < enemy.x + 40 and self.y + 40 > enemy.y and self.y < enemy.y + 40:
            self.alive = False
            timer.stop()
            self.vel_y = 0
            self.vel_x = 0

        # Tarkistetaan, ettei olla tiputtu veteen
        if self.y + 40 >= globals.SCREEN_HEIGHT - 40:
            self.alive = False
            timer.stop()
            self.vel_x = self.vel_y = 0

        # Tarkastetaan palkinnon sijainti
        for price in prices:
            if (self.x + 40 > price.x and self.x < price.x + 20 and self.y + 40 > price.y
                and self.y < price.y + 20 and not price.deleted):
                price.available = False
