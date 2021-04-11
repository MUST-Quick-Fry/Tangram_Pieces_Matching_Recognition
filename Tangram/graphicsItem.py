# package
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPolygonF
from gui import *
from PyQt5.QtWidgets import *

# graphic item class
class gItem:
    vert = []  # vertex matrix
    colorIndex = 0

    def __init__(self, vertex, colorNumber):
        self.vert = vertex
        self.colorIndex = colorNumber
        self.Item = QGraphicsPolygonItem()
        self.item = QPolygonF()
        self.Item.setFlag(QGraphicsItem.ItemIsSelectable)  # set selectable
        self.Item.setFlag(QGraphicsItem.ItemIsMovable)  # set movable
        self.drawItem()

    def drawItem(self):
        for i in range(0, len(self.vert), 2):
            self.item.append(QPointF(self.vert[i], self.vert[i+1]))

        self.Item.setPolygon(self.item)
        self.setColor(color=self.colorIndex)

    def setColor(self, color):
        if color == 1:
            self.Item.setBrush(Qt.red)
        elif color == 2:
            self.Item.setBrush(Qt.blue)
        elif color == 3:
            self.Item.setBrush(Qt.yellow)
        elif color == 4:
            self.Item.setBrush(Qt.green)
        elif color == 5:
            self.Item.setBrush(Qt.black)

        self.Item.brush()


class Graphics(QMainWindow, Ui_MainWindow):
    UNIT = 100
    width = 5 * UNIT
    height = 5 * UNIT
    coord = []
    color = 0

    def __init__(self):
        super(Graphics, self).__init__()
        self.setupUi(self)
        self.draw_graphics()

    def draw_graphics(self):

        # create a scene
        self.graphicsView.scene = QtWidgets.QGraphicsScene(0, 0, self.width, self.height)

        # draw a big triangle
        self.coord = [0, 0, 2, 0, 1, 1]  # position [x1, y1, x2, y2, x3, y3]
        self.color = 1  # set color code
        self.graphicsView.scene.addItem(gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        # set scene
        self.graphicsView.setScene(self.graphicsView.scene)
