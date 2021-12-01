import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

import Main
import second
from PyQt5 import QtCore, QtGui, QtWidgets

import third


class MyWindow(Main.Ui_MainWindow, QMainWindow):
    file = ""

    def __init__(self):
        super(Main.Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_btn_clicked)
        self.pushButton_3.clicked.connect(self.openFileNameDialog)


    def open_btn_clicked(self):
        self.aw = second.AnotherWindowActions()
        self.aw.show()
        self.close()

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                            "(*.csv);;Python Files (*.py)", options=options)
        MyWindow.file = fileName
        MyWindow.filePath = fileName
        #self.aw = second.AnotherWindowActions()
        #self.aw.setfile(MyWindow.file)
        #self.tw = third.AnotherWindowActions()
        #self.tw.setfile(MyWindow.file)
        self.label_2.setText("Path: " + fileName)
        with open("filename.txt", "w") as f:
            f.write(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
