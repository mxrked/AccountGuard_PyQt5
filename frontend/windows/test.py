from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/test.ui", self)


        # Show the app
        self.show()


# initializing app
def main():
    app = QApplication(sys.argv)
    UIWindow = UI()
    UIWindow.show()
    app.exec_()
