import sys
import Matching
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
import lanuch
import test
# import tensorFlowMatching

class AnotherWindowActions(Matching.Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(Matching.Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_btn_clicked)
        print("third: ", Matching.Ui_MainWindow.filePath)
        namelist = test.name
        count = 1
        for filename in namelist:
            self.label = QtWidgets.QLabel(self.scrollArea)
            self.label.setText(filename)
            self.label.move(10, count * 40)
            count += 1

    def open_btn_clicked(self):
        self.aw = lanuch.MyWindow()
        self.aw.show()
        self.close()


