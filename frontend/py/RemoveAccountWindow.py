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
        self.backBtn = self.findChild(QPushButton, "removeAccountWindow_BackBtn")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        # Show the app
        self.show()

        def goBack():
            '''
            This is used to go back to the start window
            :return:
            '''

            from frontend.py.StartWindow import StartWindow

            startWindow = StartWindow()
            startWindow.move(self.pos())
            startWindow.show()

            self.hide()



        # Apply functions to/style widgets
        self.backBtn.clicked.connect(goBack)

    def closeEvent(self, event):
        '''
        This is used to close the window on the red X and reopens the start window
        :param event:
        :return:
        '''

        from frontend.py.StartWindow import StartWindow

        startWindow = StartWindow()
        startWindow.move(self.pos())
        startWindow.show()

        self.hide()

# initializing app
app = QApplication(sys.argv)
UIWindow = RemoveAccountWindow()
app.exec_()