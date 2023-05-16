'''

    This is the Start Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/StartWindow.ui", self)

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
    UIWindow = UI()
    UIWindow.show()
    app.exec_()


if __name__ == "__main__":
    main()