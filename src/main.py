import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap
from scene import Scene
from menu import Menu
from camera import Camera
import globals

#lahteet: https://gist.github.com/rogerallen/f06ba704ce3befb5459239e3fdf842c7



if __name__ == '__main__':
    globals.init()

    app = QApplication(sys.argv)
    app.setApplicationName('Kario')
    icon = QIcon(QPixmap("static/kario1_right.png"))
    app.setWindowIcon(icon)
    scene = Menu()
    sys.exit(app.exec_())
