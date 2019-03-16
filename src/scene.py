from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsTextItem, QFrame
from PyQt5.QtGui import QBrush, QColor
from player import Player
from enemy import Enemy
from platform import Platform
from price import Price
from camera import Camera

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
PLAYER_SPEED            = 3   # pix/frame
FRAME_TIME_MS           = 16  # ms/frame
GRAVITY                 = 0.6



class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        self.pfset = []
        self.prices = []

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        bg = QGraphicsRectItem()
        bg.setRect(-1,-1,SCREEN_WIDTH*2 + 2,SCREEN_HEIGHT + 2)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)

        self.player = Player()
        self.addItem(self.player)

        self.platform = Platform(400, 500, 100)
        self.addItem(self.platform)
        self.pfset.append(self.platform)

        self.platform = Platform(200, 400, 100)
        self.addItem(self.platform)
        self.pfset.append(self.platform)

        self.enemy = Enemy(500)
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

        #vanha QGV
        # self.view = QGraphicsView(self)
        # self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.view.show()
        # self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        # self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

        self.view = Camera(self, self.player)
        #self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        #self.view.ensureVisible(self.player)
        #self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        #self.view.show()



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
        self.view.ensureVisible(self.player, 200, 0)
        #self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.update()

    def score_update(self, price):
        self.removeItem(price)
        price.deleted = True
        self.player.points += 1
        self.removeItem(self.points)
        self.points = QtWidgets.QGraphicsTextItem('Score: ' + str(self.player.points))
        self.points.setDefaultTextColor(QtGui.QColor(255, 255, 255))
        self.points.setFont(self.font)
        #self.points.setPos(200, 200)
        #print(self.view.mapFromScene())
        self.addItem(self.points)

    def game_update(self):
        self.player.player_update(self.keys_pressed, self.enemy, self.timer, self.pfset, self.prices, self.view)
        self.enemy.enemy_update()
        for price in self.prices:
            if price.price_update() and not price.deleted:
                self.score_update(price)
        if not self.player.alive:
            go = QtWidgets.QGraphicsTextItem('GAME OVER')
            go.setDefaultTextColor(QtGui.QColor(255, 0, 0))
            go_font = QtGui.QFont()
            go_font.setPointSize(40)
            go.setFont(go_font)
            go.setPos(200, 300)
            self.addItem(go)
