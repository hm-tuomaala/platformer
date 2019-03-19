from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt
import globals


class Camera(QGraphicsView):
    def __init__(self, scene, parent = None):
        super().__init__(scene, parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.show()
        self.setFixedSize(globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)

    def update_scene(self, scene):
        self.setScene(scene)
