'''

    This is the Remove Account Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

import sys


class RemoveAccountWindow(QMainWindow):
    def __init__(self):
        super(RemoveAccountWindow, self).__init__()

        uic.loadUi("frontend/ui/RemoveAccountWindow.ui", self)

        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        # Show the app
        self.show()


# initializing app
def main():
    app = QApplication(sys.argv)
    UIWindow = RemoveAccountWindow()
    UIWindow.show()
    app.exec_()