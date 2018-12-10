import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from design import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.point = None
        self.pushButton_00.clicked.connect(self.run)


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
                


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())