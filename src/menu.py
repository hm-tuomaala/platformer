from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsTextItem, QFrame
from PyQt5.QtGui import QBrush, QColor
import globals
from scene import Scene
from camera import Camera


class Menu(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        self.addItem(QtWidgets.QGraphicsTextItem('Mario Game'))
        rect = QGraphicsRectItem(0, 0, 100, 100)
        self.addItem(rect)
        self.view = Camera(self)
        self.view.setFixedSize(globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)
        #self.gameScene = Scene()

    def mousePressEvent(self, event):
        scene = Scene(self.view, self)
