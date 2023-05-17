'''

    This is the Add Account Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

import sys


class AddAccountWindow(QMainWindow):
    def __init__(self):
        super(AddAccountWindow, self).__init__()

        uic.loadUi("frontend/ui/AddAccountWindow.ui", self)

        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        # Show the app
        # self.show()


# initializing app
app = QApplication(sys.argv)
UIWindow = AddAccountWindow()
app.exec_()