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

        self.button1 = QGraphicsRectItem(147, 300, 104, 60)
        self.button1.setBrush(QBrush(QtGui.QColor(38, 38, 38)))
        self.addItem(self.button1)

        self.b1 = QtWidgets.QGraphicsTextItem('BACK')
        self.b1.setDefaultTextColor(QtGui.QColor(255, 0, 0))
        self.b1.setPos(150, 300)
        self.addItem(self.b1)

        self.view.update_scene(self)

    def mousePressEvent(self, QMouseEvent):
        if(QMouseEvent.scenePos().x() >= 147 and QMouseEvent.scenePos().x() <= 147+104
            and QMouseEvent.scenePos().y() >= 300 and QMouseEvent.scenePos().y() <= 300+60):
            self.view.update_scene(self.menu)
