from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import (QGraphicsItem, QGraphicsRectItem, QGraphicsScene,
                             QGraphicsView, QGraphicsTextItem, QFrame)
from PyQt5.QtGui import QBrush, QColor
from player import Player
from enemy import Enemy
from platform import Platform
from price import Price
from camera import Camera
from map import Map
from goal import Goal
import globals



class Scene(QGraphicsScene):
    def __init__(self, cam, menu, parent = None):
        QGraphicsScene.__init__(self, parent)

        self.prices = []
        self.dead = False
        self.menu = menu

        # Tallennetaan painetut nappaimet
        self.keys_pressed = set()

        self.timer = QBasicTimer()
        self.timer.start(globals.FRAME_SPEED, self)

        bg = QGraphicsRectItem()
        bg.setRect(0,0, globals.SCREEN_WIDTH*4, globals.SCREEN_HEIGHT)
        bg.setBrush(QBrush(QtGui.QColor(128, 223, 255)))
        self.addItem(bg)

        self.player = Player()
        self.addItem(self.player)


        self.map = Map()
        for i in range(int(globals.SCREEN_HEIGHT / 40)):
            for j in range(int((globals.SCREEN_WIDTH*4) / 40)):
                if self.map.map[i][j] > 0:
                    self.platform = Platform(j*40, i*40, self.map.map[i][j])
                    self.addItem(self.platform)

        self.enemy = Enemy(500, 200)
        self.addItem(self.enemy)

        self.price1 = Price(250, 350)
        self.addItem(self.price1)
        self.prices.append(self.price1)

        self.price2 = Price(750, 500)
        self.addItem(self.price2)
        self.prices.append(self.price2)

        self.price3 = Price(650, 300)
        self.addItem(self.price3)
        self.prices.append(self.price3)


        self.font = QtGui.QFont()
        self.font.setPointSize(15)

        self.points = QtWidgets.QGraphicsTextItem('Score: ' + str(self.player.points) + ' / ' + str(len(self.prices)))
        self.points.setDefaultTextColor(QtGui.QColor(38, 38, 38))
        self.points.setFont(self.font)
        self.addItem(self.points)

        self.goal = Goal(3000, 440)
        self.addItem(self.goal)


        self.view = cam
        self.view.update_scene(self)


    def mousePressEvent(self, event):
        if self.dead:
            self.view.update_scene(self.menu)

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        if event.key() != 32:
            self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.view.ensureVisible(self.player, 350, 0)
        self.update()

    def score_update(self, price):
        self.removeItem(price)
        self.removeItem(self.points)
        price.deleted = True
        self.player.points += 1
        self.points = QtWidgets.QGraphicsTextItem('Score: ' + str(self.player.points) + ' / ' + str(len(self.prices)))
        self.points.setDefaultTextColor(QtGui.QColor(38, 38, 38))
        self.points.setFont(self.font)
        self.move_score()
        self.addItem(self.points)


    def move_score(self):
        self.points.setPos(self.view.mapToScene(1, -3).x(), 0)

    def game_over(self):
        game_over = QtWidgets.QGraphicsTextItem('GAME OVER')
        game_over.setDefaultTextColor(QtGui.QColor(255, 0, 0))
        go_font = QtGui.QFont()
        go_font.setPointSize(40)
        game_over.setFont(go_font)
        game_over.setPos(self.view.mapToScene(1, -3).x() + 175, 250)
        self.addItem(game_over)
        self.dead = True


    def game_update(self):
        self.player.player_update(self.keys_pressed, self.enemy, self.timer, self.prices, self.map, self.goal)
        self.enemy.enemy_update(self.map)
        for price in self.prices:
            if price.price_update() and not price.deleted:
                self.score_update(price)
        if not self.player.alive: #Pelaaja kuoli
            self.game_over()
        self.move_score()
        if not self.enemy.alive and not self.enemy.deleted:
            self.removeItem(self.enemy)
            self.enemy.deleted = True
