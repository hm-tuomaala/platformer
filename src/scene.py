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
import json



class Scene(QGraphicsScene):
    def __init__(self, cam, menu, parent = None):
        QGraphicsScene.__init__(self, parent)

        self.prices = []
        self.time = 0
        self.menu = menu

        # Tallennetaan painetut nappaimet
        self.keys_pressed = set()

        self.timer = QBasicTimer()
        self.timer.start(globals.FRAME_SPEED, self)

        bg = QGraphicsRectItem()
        bg.setRect(0,0, globals.SCREEN_WIDTH*4, globals.SCREEN_HEIGHT)
        bg.setBrush(QBrush(QtGui.QColor(128, 191, 255)))
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

        self.points = QtWidgets.QGraphicsTextItem('Prices: ' + str(self.player.points) + ' / ' + str(len(self.prices)))
        self.points.setDefaultTextColor(QtGui.QColor(38, 38, 38))
        self.points.setFont(self.font)
        self.addItem(self.points)

        self.display = QtWidgets.QGraphicsTextItem('Time: ' + str(int(self.time)))
        self.display.setDefaultTextColor(QtGui.QColor(38, 38, 38))
        self.display.setFont(self.font)
        self.display.setPos(200, 1)
        self.addItem(self.display)

        self.goal = Goal(3000, 440)
        self.addItem(self.goal)


        self.view = cam
        self.view.update_scene(self)


    def mousePressEvent(self, event):
        if not self.player.alive:
            self.menu.update_hs()
            self.view.update_scene(self.menu)
        if self.player.win:
            self.menu.update_hs()
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
        self.time += 0.016
        self.display_update()

    def score_update(self, price):
        self.removeItem(price)
        self.removeItem(self.points)
        price.deleted = True
        self.player.points += 1
        self.points = QtWidgets.QGraphicsTextItem('Prices: ' + str(self.player.points) + ' / ' + str(len(self.prices)))
        self.points.setDefaultTextColor(QtGui.QColor(38, 38, 38))
        self.points.setFont(self.font)
        self.move_score()
        self.addItem(self.points)


    def move_score(self):
        self.points.setPos(self.view.mapToScene(1, -3).x(), 0)
        self.display.setPos(self.view.mapToScene(200, -3).x(), 0)

    def game_over(self):
        game_over = QtWidgets.QGraphicsTextItem('GAME OVER')
        game_over.setDefaultTextColor(QtGui.QColor(255, 0, 0))
        go_font = QtGui.QFont()
        go_font.setPointSize(40)
        game_over.setFont(go_font)
        game_over.setPos(self.view.mapToScene(1, -3).x() + 175, 150)
        self.addItem(game_over)

    def game_win(self):
        game_win = QtWidgets.QGraphicsTextItem('WINNER!!!')
        game_win.setDefaultTextColor(QtGui.QColor(0, 128, 0))
        go_font = QtGui.QFont()
        go_font.setPointSize(40)
        game_win.setFont(go_font)
        game_win.setPos(self.view.mapToScene(1, -3).x() + 175, 150)
        self.addItem(game_win)

        with open('static/highscore.json') as f:
            data = json.load(f)
        highscore = data["highscore"]
        if self.time < highscore:
            new_highscore = QtWidgets.QGraphicsTextItem('New Highscore: ' + str(int(self.time)))
            new_highscore.setDefaultTextColor(QtGui.QColor(0, 128, 0))
            new_highscore.setFont(self.font)
            new_highscore.setPos(self.view.mapToScene(1, -3).x() + 230, 250)
            self.addItem(new_highscore)
            with open('static/highscore.json', "w") as f:
                write = {"highscore": self.time}
                json.dump(write, f)


    def game_update(self):
        self.player.player_update(self.keys_pressed, self.enemy, self.timer, self.prices, self.map, self.goal)
        self.enemy.enemy_update(self.map)
        for price in self.prices:
            if price.price_update() and not price.deleted:
                self.score_update(price)
        #Pelaaja kuoli
        if not self.player.alive:
            self.game_over()
        if self.player.win:
            self.game_win()

        self.move_score()
        if not self.enemy.alive and not self.enemy.deleted:
            self.removeItem(self.enemy)
            self.enemy.deleted = True

    def display_update(self):
        self.removeItem(self.display)
        self.display = QtWidgets.QGraphicsTextItem('Time: ' + str(int(self.time)))
        self.display.setDefaultTextColor(QtGui.QColor(38, 38, 38))
        self.display.setFont(self.font)
        self.display.setPos(300, 1)
        self.move_score()
        self.addItem(self.display)
