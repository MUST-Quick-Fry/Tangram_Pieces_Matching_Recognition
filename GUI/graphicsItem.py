
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPolygonF

from gui import *
from PyQt5.QtWidgets import *

class Graphics(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Graphics, self).__init__()
        self.setupUi(self)
        self.draw_graphics()

    def draw_graphics(self):
        # create a scene
        self.graphicsView.scene = QtWidgets.QGraphicsScene(0, 0, 200, 200)

        # Describe a closed triangle 1
        self.tri1 = QGraphicsPolygonItem()
        self.Triangle1 = QPolygonF()
        self.Triangle1.append(QPointF(-100, -100))
        self.Triangle1.append(QPointF(300, -100))
        self.Triangle1.append(QPointF(100, 100))
        self.Triangle1.append(QPointF(-100, -100))
        self.tri1.setPolygon(self.Triangle1)
        self.tri1.setBrush(Qt.red)
        self.tri1.brush()
        self.graphicsView.scene.addItem(self.tri1)

        # Describe a closed triangle 2
        self.tri2 = QGraphicsPolygonItem()
        self.Triangle2 = QPolygonF()
        self.Triangle2.append(QPointF(-100, -100))
        self.Triangle2.append(QPointF(-100, 300))
        self.Triangle2.append(QPointF(100, 100))
        self.Triangle2.append(QPointF(-100, -100))
        self.tri2.setPolygon(self.Triangle2)
        self.tri2.setBrush(Qt.cyan)
        self.tri2.brush()
        self.graphicsView.scene.addItem(self.tri2)

        # Describe a closed triangle 3
        self.tri3 = QGraphicsPolygonItem()
        self.Triangle3 = QPolygonF()
        self.Triangle3.append(QPointF(-100, 300))
        self.Triangle3.append(QPointF(100, 300))
        self.Triangle3.append(QPointF(0, 200))
        self.Triangle3.append(QPointF(-100, 300))
        self.tri3.setPolygon(self.Triangle3)
        self.tri3.setBrush(Qt.yellow)
        self.tri3.brush()
        self.graphicsView.scene.addItem(self.tri3)

        # Describe a closed triangle 4
        self.tri4 = QGraphicsPolygonItem()
        self.Triangle4 = QPolygonF()
        self.Triangle4.append(QPointF(100, 100))
        self.Triangle4.append(QPointF(200, 200))
        self.Triangle4.append(QPointF(200, 0))
        self.Triangle4.append(QPointF(100, 100))
        self.tri4.setPolygon(self.Triangle4)
        self.tri4.setBrush(Qt.gray)
        self.tri4.brush()
        self.graphicsView.scene.addItem(self.tri4)

        # Describe a closed triangle 5
        self.tri5 = QGraphicsPolygonItem()
        self.Triangle5 = QPolygonF()
        self.Triangle5.append(QPointF(300, 100))
        self.Triangle5.append(QPointF(300, 300))
        self.Triangle5.append(QPointF(100, 300))
        self.Triangle5.append(QPointF(300, 100))
        self.tri5.setPolygon(self.Triangle5)
        self.tri5.setBrush(Qt.black)
        self.tri5.brush()
        self.graphicsView.scene.addItem(self.tri5)

        # Describe a closed rectangle
        self.rect = QGraphicsPolygonItem()
        self.Rectangle = QPolygonF()
        self.Rectangle.append(QPointF(100, 300))
        self.Rectangle.append(QPointF(0, 200))
        self.Rectangle.append(QPointF(100, 100))
        self.Rectangle.append(QPointF(200, 200))
        self.Rectangle.append(QPointF(100, 300))
        self.rect.setPolygon(self.Rectangle)
        self.rect.setBrush(Qt.blue)
        self.rect.brush()
        self.graphicsView.scene.addItem(self.rect)

        # Describe a closed parallelogram
        self.rect = QGraphicsPolygonItem()
        self.Rectangle = QPolygonF()
        self.Rectangle.append(QPointF(200, 200))
        self.Rectangle.append(QPointF(200, 0))
        self.Rectangle.append(QPointF(300, -100))
        self.Rectangle.append(QPointF(300, 100))
        self.Rectangle.append(QPointF(200, 200))
        self.rect.setPolygon(self.Rectangle)
        self.rect.setBrush(Qt.green)
        self.rect.brush()
        self.graphicsView.scene.addItem(self.rect)

        # set scene
        self.graphicsView.setScene(self.graphicsView.scene)
