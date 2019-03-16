import sys
from PyQt5.QtWidgets import QApplication
from scene import Scene




if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())
