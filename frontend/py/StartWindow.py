'''

    This is the Start Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.assets.qrc import background_gradient, app_icon, lock_icon
from frontend.assets.funcs.display_success_error_label import display_success_error_label

import sys


class StartWindow(QMainWindow):


    def __init__(self):
        super(StartWindow, self).__init__()

        uic.loadUi("frontend/ui/StartWindow.ui", self)

        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.bothDetectedLabel = self.findChild(QLabel, "startWindow_BothDetectedLabel")
        self.bothNotDetectedLabel = self.findChild(QLabel, "startWindow_BothNotFoundLabel")
        self.sSMSNotDetectedLabel = self.findChild(QLabel, "startWindow_SSMSNotFoundLabel")
        self.oDBCNotDetectedLabel = self.findChild(QLabel, "startWindow_ODBCNotFoundLabel")
        self.addAccountBtn = self.findChild(QPushButton, "startWindow_AddAccountBtn")
        self.removeAccountBtn = self.findChild(QPushButton, "startWindow_RemoveAccountBtn")
        self.viewAccountsBtn = self.findChild(QPushButton, "startWindow_ViewAccountsBtn")
        self.exitCloseBtn = self.findChild(QPushButton, "startWindow_ExitCloseBtn")
        self.infoBtn = self.findChild(QPushButton, "startWindow_InfoBtn")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def exitApp():
            '''
            This is used to close the app
            :return:
            '''
            sys.exit()

        def openAddAccountWindow():
            '''
            This is used to open the add account window
            :return:
            '''

            from frontend.py import AddAccountWindow

            AddAccountWindow.UIWindow.move(self.pos())
            AddAccountWindow.UIWindow.show()
            self.hide()

        def openRemoveAccountWindow():
            '''
            This is used to open the remove account window
            :return:
            '''

            from frontend.py import RemoveAccountWindow

            RemoveAccountWindow.UIWindow.move(self.pos())
            RemoveAccountWindow.UIWindow.show()
            self.hide()

        def openViewAccountsWindow():
            '''
            This is used to open the view accounts window
            :return:
            '''

            from frontend.py import ViewAccountsWindow

            ViewAccountsWindow.UIWindow.move(self.pos())
            ViewAccountsWindow.UIWindow.show()
            self.hide()


        # Apply functions to/style widgets
        self.addAccountBtn.clicked.connect(openAddAccountWindow)
        self.removeAccountBtn.clicked.connect(openRemoveAccountWindow)
        self.viewAccountsBtn.clicked.connect(openViewAccountsWindow)
        self.exitCloseBtn.clicked.connect(exitApp)


        # Displaying result of program detection
        display_success_error_label(self)


        # Show the app
        self.show()


# initializing app

def main():
    app = QApplication(sys.argv)
    UIWindow = StartWindow()
    UIWindow.show()
    app.exec_()
