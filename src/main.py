import sys
from PyQt5.QtWidgets import QApplication
from scene import Scene
from menu import Menu
from camera import Camera
import globals

#lahteet: https://gist.github.com/rogerallen/f06ba704ce3befb5459239e3fdf842c7



if __name__ == '__main__':
    globals.init()

    app = QApplication(sys.argv)
    app.setApplicationName('Mario')
    #scene = Scene()
    scene = Menu()
    sys.exit(app.exec_())
