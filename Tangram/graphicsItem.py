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
        elif color == 6:
            self.Item.setBrush(Qt.cyan)
        elif color == 7:
            self.Item.setBrush(Qt.gray)
        self.Item.brush()


class Graphics(QMainWindow, Ui_MainWindow):
    UNIT = 100
    width = 5 * UNIT
    height = 5 * UNIT
    coord = []
    color = 0

    def __init__(self,parent=None):
        super(Graphics, self).__init__(parent)
        self.setupUi(self)

        #namespace _translate
        _translate = QtCore.QCoreApplication.translate
        self.comboBox.setItemText(0, _translate("MainWindow", "Case"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Case1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Case2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Case3"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Case4"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Case5"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Case6"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Case7"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Case8"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Case9"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Case10"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Case11"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Case12"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Case13"))
        self.comboBox.currentIndexChanged.connect(self.draw_graphics)

        self.comboBox_2.setItemText(0, _translate("MainWindow", "Algorithm"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "DFS"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "BFS"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "IDA"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "A*"))
        self.label_2.setText(_translate("MainWindow", "Quantity of Methods: "))
        self.label_3.setText(_translate("MainWindow", "7"))

    def draw_graphics(self,text):

        # create a scene
        self.graphicsView.scene = QtWidgets.QGraphicsScene(0, 0, self.width, self.height)

        text = self.comboBox.currentText()
        if text=='Case1':
            self.graphicsView.scene.clear()
            # draw a big triangle
            self.coord = [-1,4,3,4,1,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,4,7,4,5,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,4,2,3,4,3]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,1,3,2,3,0]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,0,3,2,5,2]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [1,2,2,1,3,2,2,3]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,3,4,3,5,2,3,2]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case2':
            self.graphicsView.scene.clear()
            self.coord = [0, 0, 4, 0, 2, 2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0, 0, 0, 4, 2, 2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0, 4, 2, 4, 1, 3]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2, 2, 3, 3, 3, 1]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4, 2, 4, 4, 2, 4]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2, 4, 1, 3, 2, 2, 3, 3]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3, 3, 3, 1, 4, 0, 4, 2]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case3':
            self.graphicsView.scene.clear()
            self.coord = [0,4,2,6,2,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,6,2,2,4,4]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,2,3,1,4,2]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [5,1,5,3,6,2]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,2,4,4,4,2]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,0,3,1,4,2,5,1]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,2,4,4,5,3,5,1]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case4':
            self.graphicsView.scene.clear()
            self.coord = [0,4,4,4,2,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,0,8,0,6,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,2,3,1,4,2]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [5,1,6,2,5,3]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,2,4,2,4,4]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,0,3,1,4,2,5,1]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,2,4,4,5,3,5,1]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case5':
            self.graphicsView.scene.clear()
            self.coord = [0,2,0,6,2,4]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,0,6,0,4,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,2,1,1,1,3]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,2,4,2,3,3]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,0,2,2,4,2]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [1,3,2,2,3,3,2,4]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [1,3,2,2,2,0,1,1]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case6':
            self.graphicsView.scene.clear()
            # draw a big triangle
            self.coord = [0,6,0,2,2,4]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,2,2,4,2,0]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,0,2,2,3,1]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,0,3,1,5,1]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,1,5,1,3,3]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,-1,2,0,3,1,4,0]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,2,2,4,3,3,3,1]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case7':
            self.graphicsView.scene.clear()
            # draw a big triangle
            self.coord = [0,0,0,4,2,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,4,6,4,4,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,0,2,0,1,1]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,1,3,3,4,2]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,4,2,4,2,2]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,0,1,1,2,2,3,1]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,2,2,4,3,3,3,1]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case8':
            self.graphicsView.scene.clear()
            self.coord = [2,1,0,3,4,3]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,0,5,2,7,0]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,1,3,2,5,2]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,2,4,3,5,2]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,3,6,3,6,1]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,0,2,1,3,2,4,1]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [7,0,6,1,6,3,7,2,7,0]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case9':
            self.graphicsView.scene.clear()
            self.coord = [0,0,0,4,2,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,0,2,2,4,0]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,4,1,5,1,3]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,1,2,2,4,2]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [1,3,1,5,3,3]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,0,3,1,4,2,5,1]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,2,1,3,3,3,4,2]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case10':
            self.graphicsView.scene.clear()
            self.coord = [2,0,0,2,4,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,2,2,4,4,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,4,4,4,3,3]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [5,1,5,3,6,2]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,0,4,2,4,0]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,2,3,3,4,4,5,3]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,0,4,2,5,3,5,1]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case11':
            self.graphicsView.scene.clear()
            self.coord = [2,0,0,2,4,2]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,0,4,2,6,0]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,2,3,3,4,2]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [5,1,5,3,6,2]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [5,1,3,3,5,3]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [6,0,5,1,6,2,7,1]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,2,1,3,3,3,2,2]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case12':
            self.graphicsView.scene.clear()
            # draw a big triangle
            self.coord = [2,1,0,3,2,5]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,1,2,5,4,3]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,0,2,1,3,2]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,0,3,2,4,1]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,1,0,3,2,1]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,1,3,2,4,3,5,2]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [1,0,0,1,2,1,3,0]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        elif text=='Case13':
            self.graphicsView.scene.clear()
            self.coord = [2,1,0,3,2,5]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,1,2,5,4,3]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,1,3,2,4,1]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [5,0,4,1,5,2]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,3,0,5,2,5]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,1,3,2,4,3,5,2]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,0,2,1,4,1,5,0]
            self.color = 7
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

        # set scene
        self.graphicsView.setScene(self.graphicsView.scene)
