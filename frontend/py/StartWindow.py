'''

    This is the Start Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.assets.qrc import background_gradient, app_icon, lock_icon
from frontend.assets.funcs.detect_required_programs import check_for_required_programs


# from frontend.assets.sample_code.locating_odbc_drivers import detect_odbc_drivers
# from frontend.assets.sample_code.locating_ssms import ssms_installation_location

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

            AddAccountWindow.UIWindow.show()
            self.hide()

        def openRemoveAccountWindow():
            '''
            This is used to open the remove account window
            :return:
            '''

            from frontend.py import RemoveAccountWindow

            RemoveAccountWindow.UIWindow.show()
            self.hide()


        # Apply functions to/style widgets
        self.addAccountBtn.clicked.connect(openAddAccountWindow)
        self.removeAccountBtn.clicked.connect(openRemoveAccountWindow)
        self.exitCloseBtn.clicked.connect(exitApp)


        # Displaying result of program detection
        if (check_for_required_programs == "SSMS was not found"):
            self.sSMSNotDetectedLabel.setFixedHeight(50)

        if (check_for_required_programs == "ODBC was not found"):
            self.oDBCNotDetectedLabel.setFixedHeight(50)

        if (check_for_required_programs == "Both programs were not found"):
            self.bothNotDetectedLabel.setFixedHeight(50)

        if (check_for_required_programs == "Both programs were found"):
            self.bothDetectedLabel.setFixedHeight(50)


        # Show the app
        self.show()


# initializing app
def main():
    app = QApplication(sys.argv)
    UIWindow = StartWindow()
    UIWindow.show()
    app.exec_()


if __name__ == "__main__":
    main()