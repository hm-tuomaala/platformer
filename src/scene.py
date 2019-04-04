from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsTextItem, QFrame
from PyQt5.QtGui import QBrush, QColor
from player import Player
from enemy import Enemy
from platform import Platform
from price import Price
from camera import Camera
from map import Map
import globals



class Scene(QGraphicsScene):
    def __init__(self, cam, menu, parent = None):
        QGraphicsScene.__init__(self, parent)

        self.pfset = []
        self.prices = []
        self.dead = False
        self.menu = menu

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(globals.FRAME_SPEED, self)

        bg = QGraphicsRectItem()
        bg.setRect(0,0, globals.SCREEN_WIDTH*2, globals.SCREEN_HEIGHT)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)

        self.player = Player()
        self.addItem(self.player)

        # self.platform = Platform(400, 500, 100)
        # self.addItem(self.platform)
        # self.pfset.append(self.platform)
        #
        # self.platform = Platform(200, 400, 100)
        # self.addItem(self.platform)
        # self.pfset.append(self.platform)

        self.map = Map()
        for i in range(int(globals.SCREEN_HEIGHT / 40)):
            for j in range(int((globals.SCREEN_WIDTH * 2) / 40)):
                if self.map.map[i][j] == 1:
                    self.platform = Platform(j*40, i*40)
                    self.addItem(self.platform)
                    self.pfset.append(self.platform)

        self.enemy = Enemy(500, 400)
        self.addItem(self.enemy)

        self.price1 = Price(250, 350)
        self.addItem(self.price1)
        self.prices.append(self.price1)

        self.price2 = Price(750, 500)
        self.addItem(self.price2)
        self.prices.append(self.price2)


        self.font = QtGui.QFont()
        self.font.setPointSize(15)

        self.points = QtWidgets.QGraphicsTextItem('Score: ' + str(self.player.points))
        self.points.setDefaultTextColor(QtGui.QColor(255, 255, 255))
        self.points.setFont(self.font)
        self.addItem(self.points)



        self.view = cam
        self.view.update_scene(self)


    def mousePressEvent(self, event):
        if self.dead:
            self.view.update_scene(self.menu)

    def keyPressEvent(self, event):
        # if event.key() == 32 and 32 in self.keys_pressed:
        #     pass
        # else:
        #     self.keys_pressed.add(event.key())

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
        self.points = QtWidgets.QGraphicsTextItem('Score: ' + str(self.player.points))
        self.points.setDefaultTextColor(QtGui.QColor(255, 255, 255))
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
        self.player.player_update(self.keys_pressed, self.enemy, self.timer, self.pfset, self.prices, self.map)
        self.enemy.enemy_update()
        for price in self.prices:
            if price.price_update() and not price.deleted:
                self.score_update(price)
        if not self.player.alive: #Player died
            self.game_over()
        self.move_score()
