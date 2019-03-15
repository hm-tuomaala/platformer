from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QBrush
from player import Player
from enemy import Enemy
from platform import Platform

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
PLAYER_SPEED            = 3   # pix/frame
FRAME_TIME_MS           = 16  # ms/frame
GRAVITY                 = 0.6



class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        self.pfset = []

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        bg = QGraphicsRectItem()
        bg.setRect(-1,-1,SCREEN_WIDTH+2,SCREEN_HEIGHT+2)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)

        self.player = Player()
        #self.player.setPos(0, 0)
        self.addItem(self.player)

        self.platform = Platform(400, 500, 100)
        self.addItem(self.platform)
        self.pfset.append(self.platform)

        self.platform = Platform(200, 400, 100)
        self.addItem(self.platform)
        self.pfset.append(self.platform)

        self.enemy = Enemy(500)
        self.addItem(self.enemy)

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

    def keyPressEvent(self, event):
        if event.key() == 32 and 32 in self.keys_pressed:
            pass
        else:
            self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        if event.key() != 32:
            self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player.player_update(self.keys_pressed, self.enemy, self.timer, self.pfset)
        self.enemy.enemy_update()
