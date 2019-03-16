from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt


class Camera(QGraphicsView):
    def __init__(self, scene, player, parent = None):
        super().__init__(scene, parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.show()
