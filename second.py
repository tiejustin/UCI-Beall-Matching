import sys
import AfterMatching
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
import launch
import test
import third
import tensorFlowMatching


class AnotherWindowActions(AfterMatching.Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(AfterMatching.Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_btn_clicked)
        self.pushButton_2.clicked.connect(self.open_third)
        #print("?:", AfterMatching.Ui_MainWindow.filePath)
        # namelist = test.name
        self.filename = ""
        with open("filename.txt", "r") as f:
            line1 = f.readline().strip()
            self.filename = line1
        name_list = tensorFlowMatching.getProjectNames(self.filename)[1:]
        count = 1
        for name in name_list:
            self.label = QtWidgets.QLabel(self.scrollArea)
            self.label.setText(name)
            self.label.move(10, count * 40)
            count += 1

    def open_btn_clicked(self):
        self.aw = launch.MyWindow()
        self.aw.show()
        self.close()

    def open_third(self):
        self.aw = third.AnotherWindowActions()
        self.aw.show()
        self.close()
