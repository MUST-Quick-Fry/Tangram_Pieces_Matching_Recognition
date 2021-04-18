# package
from gui import *
from PyQt5.QtWidgets import *
from graphicItem import gItem
import Utils

class GUI_INIT(QMainWindow, Ui_MainWindow):
    UNIT = 100
    width = 8 * UNIT
    height = 150 * UNIT
    coord = []
    color = 0

    def __init__(self, parent=None):
        super(GUI_INIT, self).__init__(parent)
        self.setupUi(self)
        self.graphicsView.scene = QtWidgets.QGraphicsScene(0, 0, self.width, self.height)   # create a scene
        self.comboBox.currentIndexChanged.connect(self.setCase)
        self.comboBox_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.drawAnswer)

    def quickDrawTangram(self, gList, scalar, PosX, PosY):
        for j in range(0, 7):
            self.coord = gList[j]  # position [x1, y1, x2, y2, x3, y3 ...]
            self.color = j + 1  # set color
            v = [i * self.UNIT/scalar for i in self.coord]
            for xi in range(0, len(v), 2):
                v[xi] = v[xi] + PosX * 2 * self.UNIT
            for yi in range(1, len(v), 2):
                v[yi] = v[yi] + PosY * 2 * self.UNIT

            self.graphicsView.scene.addItem(
                gItem(vertex=v, colorNumber=self.color).Item)

    def drawAnswer(self):
        self.graphicsView.scene.clear()
        arg1 = self.comboBox.currentIndex() - 1
        arg2 = self.comboBox_2.currentIndex() + 1

        ansList = Utils.exeParse(arg1, arg2)
        self.label_3.setText(str(len(ansList)))
        index = 0
        for glist in ansList:
            self.quickDrawTangram(gList=glist, scalar=5, PosX=index % 4, PosY=0.25 + index//4)
            index = index + 1

    def setCase(self):
        self.graphicsView.scene.clear()
        self.comboBox_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        text = self.comboBox.currentText()

        if text=='Case':
            self.comboBox_2.setEnabled(False)
            self.pushButton.setEnabled(False)

        elif text=='Case1':
            # position [x1, y1, x2, y2, x3, y3]
            glist = [[0, 4, 4, 4, 2, 2], [4, 4, 8, 4, 6, 2], [4, 4, 3, 3, 5, 3], [3, 1, 4, 2, 4, 0], [4, 0, 4, 2, 6, 2],
                     [2, 2, 3, 1, 4, 2, 3, 3], [3, 3, 5, 3, 6, 2, 4, 2]]
            self.quickDrawTangram(gList=glist, scalar=1, PosX=0, PosY=0.5)

        elif text=='Case2':
            glist = [[0, 0, 4, 0, 2, 2], [0, 0, 0, 4, 2, 2], [0, 4, 2, 4, 1, 3], [2, 2, 3, 3, 3, 1], [4, 2, 4, 4, 2, 4],
                     [2, 4, 1, 3, 2, 2, 3, 3], [3, 3, 3, 1, 4, 0, 4, 2]]
            self.quickDrawTangram(gList=glist, scalar=1, PosX=0, PosY=0.5)

        elif text=='Case3':
            glist = [[0, 4, 2, 6, 2, 2], [2, 6, 2, 2, 4, 4], [2, 2, 3, 1, 4, 2], [5, 1, 5, 3, 6, 2], [2, 2, 4, 4, 4, 2],
            [4, 0, 3, 1, 4, 2, 5, 1], [4, 2, 4, 4, 5, 3, 5, 1]]
            self.quickDrawTangram(gList=glist, scalar=1, PosX=0, PosY=0.25)

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
            self.coord = [0,7,0,3,2,5]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 1  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [0,3,2,5,2,1]  # position [x1, y1, x2, y2, x3, y3]
            self.color = 2  # set color code
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,1,2,3,3,2]
            self.color = 3
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [4,1,3,2,5,2]
            self.color = 4
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,2,5,2,3,4]
            self.color = 5
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [3,0,2,1,3,2,4,1]
            self.color = 6
            self.graphicsView.scene.addItem(
                gItem(vertex=[i * self.UNIT for i in self.coord], colorNumber=self.color).Item)

            self.coord = [2,3,2,5,3,4,3,2]
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