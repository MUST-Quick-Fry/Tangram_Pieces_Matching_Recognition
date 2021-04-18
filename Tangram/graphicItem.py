# package
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPolygonF
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
        elif color == 6:
            self.Item.setBrush(Qt.cyan)
        elif color == 7:
            self.Item.setBrush(Qt.gray)
        self.Item.brush()
