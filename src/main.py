import sys
from PyQt5.QtWidgets import QApplication
from scene import Scene
import globals



if __name__ == '__main__':
    globals.init()

    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())
