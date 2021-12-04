import sys
import Matching
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
import launch
import test
import tensorFlowMatching
import user_attribute

class AnotherWindowActions(Matching.Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(Matching.Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_btn_clicked)
        #print("abc: ", Matching.Ui_MainWindow.filePath)
        #namelist = test.name
        self.filename = ""
        with open("filename.txt", "r") as f:
            line1 = f.readline().strip()
            self.filename = line1
        name_list, matching_list = tensorFlowMatching.run(self.filename)
        with open("result.txt", "w") as f:
            for i in range(len(name_list)):
                f.write("{}->{}\n".format(name_list[i], matching_list[i]))
        count = 1
        for i in range(len(name_list)):
            for j in matching_list[i]:
                self.label = QtWidgets.QLabel(self.scrollArea)
                self.label.setText("{}->{}".format(name_list[i], j))
                self.label.move(3, count * 30)
                count += 1

        # self.label = QtWidgets.QLabel(self.scrollArea)
        # self.label.setText("{} -> {}".format("Shaka", "Kain Sosa"))
        # self.label.move(3, 1 * 30)
        # self.label1 = QtWidgets.QLabel(self.scrollArea)
        # self.label1.setText("{} -> {}".format("Shaka", "Ross Epstein"))
        # self.label1.move(3, 2 * 30)
        # self.label2 = QtWidgets.QLabel(self.scrollArea)
        # self.label2.setText("{} -> {}".format("Shaka", "Garrett Brown"))
        # self.label2.move(3, 3 * 30)
        # self.label3 = QtWidgets.QLabel(self.scrollArea)
        # self.label3.setText("{} -> {}".format("Online Open Mic", "Herbert Meistrich"))
        # self.label3.move(3, 4 * 30)
        # self.label4 = QtWidgets.QLabel(self.scrollArea)
        # self.label4.setText("{} -> {}".format("Online Open Mic", "Scott Sorrell"))
        # self.label4.move(3, 5 * 30)
        # self.label5 = QtWidgets.QLabel(self.scrollArea)
        # self.label5.setText("{} -> {}".format("Online Open Mic", "Neil Sahota"))
        # self.label5.move(3, 6 * 30)
        # self.label6 = QtWidgets.QLabel(self.scrollArea)
        # self.label6.setText("{} -> {}".format("Online Open Mic", "Scott Fox"))
        # self.label6.move(3, 7 * 30)
        # self.label7 = QtWidgets.QLabel(self.scrollArea)
        # self.label7.setText("{} -> {}".format("Online Open Mic", "Sasha Talebi"))
        # self.label7.move(3, 8 * 30)


    def open_btn_clicked(self):
        self.aw = launch.MyWindow()
        self.aw.show()
        self.close()


