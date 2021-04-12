
from PyQt5.QtWidgets import *
from guiEvent import GUI_INIT
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = GUI_INIT()
    main.show()
    sys.exit(app.exec())
