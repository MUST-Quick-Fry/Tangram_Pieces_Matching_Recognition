
from PyQt5.QtWidgets import *
from graphicsItem import Graphics
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Graphics()
    main.show()
    sys.exit(app.exec())
