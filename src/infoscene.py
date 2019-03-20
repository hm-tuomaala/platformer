from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import (QGraphicsItem, QGraphicsRectItem, QGraphicsScene,
                             QGraphicsView, QGraphicsTextItem, QFrame)
from PyQt5.QtGui import QBrush, QColor
import globals


class Infoscene(QGraphicsScene):
    def __init__(self, cam, menu, parent = None):
        QGraphicsScene.__init__(self, parent)
        self.view = cam
        self.menu = menu

        bg = QGraphicsRectItem()
        bg.setRect(0,0, globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)

        self.button1 = QGraphicsRectItem(40, 500, 110, 60)
        self.button1.setBrush(QBrush(QtGui.QColor(38, 38, 38)))
        self.addItem(self.button1)

        self.buttonFont = QtGui.QFont()
        self.buttonFont.setPointSize(20)
        self.textFont = QtGui.QFont()
        self.textFont.setPointSize(18)
        self.titleFont = QtGui.QFont()
        self.titleFont.setPointSize(30)

        self.b1 = QtWidgets.QGraphicsTextItem('BACK')
        self.b1.setDefaultTextColor(QtGui.QColor(255, 0, 0))
        self.b1.setPos(43, 500)
        self.b1.setFont(self.buttonFont)
        self.addItem(self.b1)

        self.title = QtWidgets.QGraphicsTextItem('How To Play')
        self.title.setDefaultTextColor(QtGui.QColor(255, 0, 0))
        self.title.setPos(200, 25)
        self.title.setFont(self.titleFont)
        self.addItem(self.title)

        text = ('The player can move with left and right arrow keys and jump with space. '
                + 'Points are awarded by collecting small red awards but be aware of '
                + 'green enemys: If you touch them you die! If you can get to the '
                + 'goal you win the level!')
        self.text = QtWidgets.QGraphicsTextItem(text)
        self.text.setDefaultTextColor(QtGui.QColor(255, 255, 255))
        self.text.setPos(150, 130)
        self.text.setFont(self.textFont)
        self.text.adjustSize()
        self.addItem(self.text)

        self.view.update_scene(self)
        #self.view.ensureVisible(bg)

    def mousePressEvent(self, QMouseEvent):
        if(QMouseEvent.scenePos().x() >= 40 and QMouseEvent.scenePos().x() <= 40+110
            and QMouseEvent.scenePos().y() >= 500 and QMouseEvent.scenePos().y() <= 500+60):
            self.view.update_scene(self.menu)
