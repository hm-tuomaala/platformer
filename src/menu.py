from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import (QGraphicsItem, QGraphicsRectItem,
QGraphicsScene, QGraphicsView, QGraphicsTextItem, QFrame)
from PyQt5.QtGui import QBrush, QColor
import globals
from scene import Scene
from camera import Camera


class Menu(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)
        self.view = Camera(self)
        bg = QGraphicsRectItem()
        bg.setRect(0,0, globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)

        self.titleFont = QtGui.QFont()
        self.titleFont.setPointSize(40)
        self.buttonFont = QtGui.QFont()
        self.buttonFont.setPointSize(20)

        self.title = QtWidgets.QGraphicsTextItem('Mario Game')
        self.title.setDefaultTextColor(QtGui.QColor(255, 0, 0))
        self.title.setFont(self.titleFont)
        self.title.setPos(190, 100)

        self.b1 = QtWidgets.QGraphicsTextItem('PLAY')
        self.b1.setDefaultTextColor(QtGui.QColor(255, 0, 0))
        self.b1.setFont(self.buttonFont)
        self.b1.setPos(150, 300)

        self.b2 = QtWidgets.QGraphicsTextItem('INFO')
        self.b2.setDefaultTextColor(QtGui.QColor(255, 0, 0))
        self.b2.setFont(self.buttonFont)
        self.b2.setPos(550, 300)

        button1 = QGraphicsRectItem(147, 300, 104, 60)
        button1.setBrush(QBrush(QtGui.QColor(38, 38, 38)))

        button2 = QGraphicsRectItem(547, 300, 106, 60)
        button2.setBrush(QBrush(QtGui.QColor(38, 38, 38)))

        self.addItem(button1)
        self.addItem(button2)
        self.addItem(self.title)
        self.addItem(self.b1)
        self.addItem(self.b2)


        self.view.ensureVisible(bg)


    def mousePressEvent(self, QMouseEvent):
        #scene = Scene(self.view, self)
        #print(str(QMouseEvent.scenePos().x()), str(QMouseEvent.scenePos().y()))
        if QMouseEvent.scenePos().x() >= 147 and QMouseEvent.scenePos().x() <= 147+104 and QMouseEvent.scenePos().y() >= 300 and QMouseEvent.scenePos().y() <= 300+60:
            scene = Scene(self.view, self)
