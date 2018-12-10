import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from design import Ui_MainWindow
from classes_N_functions import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.point = None
        self.pushButton_00.clicked.connect(self.run)
        self.new_gameButton.clicked.connect(self.new_game)
        self.game = Board()
        print(type(self.game.desk[0][1]) == BlackShashka)


    def new_game(self):
        self.game = Board()
        self.update()


    def run(self):
        self.point = True
        self.update()


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_cell(qp)
        qp.end()


    def draw_cell(self, qp):
        qp.setBrush(QColor(254, 246, 201))
        for y in range(122, 730, 162):
            for x in range(172, 800, 162):
                qp.drawRect(x, y, 78, 78)
        for y in range(203, 820, 162):
            for x in range(253, 890, 162):
                qp.drawRect(x, y, 78, 78)
        qp.setBrush(QColor(146, 97, 0))
        for y in range(122, 730, 162):
            for x in range(253, 800, 162):
                qp.drawRect(x, y, 78, 78)
        for y in range(203, 820, 162):
            for x in range(172, 810, 162):
                qp.drawRect(x, y, 78, 78)
        for y in range(8):
            for x in range(8):
                self.color = type(self.game.desk[x][y])
                if self.color == BlackShashka:
                    qp.setBrush(QColor(0, 0, 0))
                    qp.drawEllipse(172 + 81 * y, 122 + 81 * x, 78, 78)
                elif self.color == WhiteShashka:
                    qp.setBrush(QColor(255, 255, 255))
                    qp.drawEllipse(172 + 81 * y, 122 + 81 * x, 78, 78)                    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())