# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1395, 815)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 551, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QtCore.QRect(370, 100, 981, 661))
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 520, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 230, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 330, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 330, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1395, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tangram_Pieces_Matching-Recognition"))
        self.pushButton.setText(_translate("MainWindow", "Solve"))
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
        self.comboBox_2.setItemText(0, _translate("MainWindow", "DFS"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "BFS"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "A*"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "SA"))
        self.label_2.setText(_translate("MainWindow", "Methods : "))
        self.label_3.setText(_translate("MainWindow", "0"))
