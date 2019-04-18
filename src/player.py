from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsPixmapItem
from PyQt5.QtGui import QBrush, QPixmap
from PyQt5.QtCore import Qt
import globals
import math




class Player(QGraphicsPixmapItem):
    def __init__(self, parent = None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.x = 80
        self.y = 100
        self.vel_x = 0
        self.vel_y = 0
        self.counter = 0

        #dir0: oikealle, dir1: vasemmalle
        self.dir = 0
        self.score = 0

        #animaatio
        self.animations_right = [QPixmap("static/kario2_right.png"), QPixmap("static/kario3_right.png"), QPixmap("static/kario2_right.png"), QPixmap("static/kario5_right.png")]
        self.animations_left = [QPixmap("static/kario2_left.png"), QPixmap("static/kario3_left.png"), QPixmap("static/kario2_left.png"), QPixmap("static/kario5_left.png")]


        self.setPixmap(QPixmap("static/kario1_right.png"))
        self.setPos(self.x, self.y)

        self.lift = -17
        self.can_jump = False
        self.points = 0
        self.alive = True
        self.win = False

    def set_player(self, x, y):
        self.setPos(x, y)


    def move(self, keys_pressed):
        if Qt.Key_Left in keys_pressed:
            self.vel_x += -globals.PLAYER_SPEED
            self.counter += 0.15
            self.dir = 1

        if Qt.Key_Right in keys_pressed:
            self.vel_x += globals.PLAYER_SPEED
            self.counter += 0.15
            self.dir = 0

        if Qt.Key_Right not in keys_pressed and Qt.Key_Left not in keys_pressed:
            self.counter = 0
            if self.dir == 0:
                self.setPixmap(QPixmap("static/kario1_right.png"))
            else:
                self.setPixmap(QPixmap("static/kario1_left.png"))

        if Qt.Key_Space in keys_pressed:
            keys_pressed.remove(Qt.Key_Space)
            if self.vel_y == 0 and self.can_jump:
                self.vel_y = self.lift
                self.can_jump = False


    def player_update(self, keys_pressed, enemy, timer, prices, map, goal):

        self.move(keys_pressed)
        if not self.can_jump:
            if self.dir == 0:
                self.setPixmap(QPixmap("static/kario4_right.png"))
            else:
                self.setPixmap(QPixmap("static/kario4_left.png"))
        elif self.counter != 0:
            if self.dir == 0:
                self.setPixmap(self.animations_right[math.floor(self.counter % 4)])
            else:
                self.setPixmap(self.animations_left[math.floor(self.counter % 4)])

        # Painovoima
        self.vel_y += globals.GRAVITY

        if self.vel_x > 4.8:
            self.vel_x = 4.8
        if self.vel_x < -4.8:
            self.vel_x = -4.8
        if self.vel_x < 0.6 and self.vel_x > -0.6:
            self.vel_x = 0


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

        if self.can_jump:
            self.vel_x *= 0.85
        else:
            self.vel_x *= 0.985


        # Tarkastetaan vihollisen sijainti
        if self.collidesWithItem(enemy) and enemy.alive:
            if self.y + 5 < enemy.y:
                for i in range(10):
                    self.vel_y += -3.3
                enemy.alive = False
            else:
                self.alive = False
                timer.stop()
                self.vel_y = 0
                self.vel_x = 0

        #Tarkistetaan ollaanko maalissa ja tehdaan animaatio
        if self.collidesWithItem(goal) and self.score == len(prices):
            goal.victory = True
        if goal.victory:
            goal.counter += 0.1
            if goal.counter >= 6.9:
                goal.counter = 6.9
                self.win = True
                timer.stop()
            goal.setPixmap(goal.animation[math.floor(goal.counter % 7)])


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
                self.score += 1
