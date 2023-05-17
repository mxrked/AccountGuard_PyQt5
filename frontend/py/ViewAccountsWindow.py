'''

    This is the View Accounts Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

import sys


class ViewAccountsWindow(QMainWindow):
    def __init__(self):
        super(ViewAccountsWindow, self).__init__()

        uic.loadUi("frontend/ui/ViewAccountsWindow.ui", self)

        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        # Show the app
        self.show()


# initializing app
app = QApplication(sys.argv)
UIWindow = ViewAccountsWindow()
app.exec_()