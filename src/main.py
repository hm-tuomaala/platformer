import sys
from PyQt5.QtWidgets import QApplication
from scene import Scene
from menu import Menu
from camera import Camera
import globals



if __name__ == '__main__':
    globals.init()

    app = QApplication(sys.argv)
    app.setApplicationName('Mario')
    #scene = Scene()
    scene = Menu()
    sys.exit(app.exec_())
