'''

    This is the Start Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.assets.qrc import background_gradient, app_icon, lock_icon
from frontend.assets.funcs.display_success_error_label import display_success_error_label
from backend.database.accessing_db import closeConnectionToDB
from backend.database.displaying_data import *


import sys, pyodbc



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
        self.onlySSMSDriversFoundLabel = self.findChild(QLabel, "startWindow_OnlySSMSDriversFoundLabel")
        self.failedToConnectLabel = self.findChild(QLabel, "startWindow_FailedDBConnectLabel")
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
            closeConnectionToDB(self)
            sys.exit()



        def openAddAccountWindow():
            '''
            This is used to open the add account window
            :return:
            '''

            from frontend.windows import AddAccountWindow

            AddAccountWindow.UIWindow.move(self.pos())
            AddAccountWindow.UIWindow.show()

            displayAllAccounts(self)
            displayAllTypes(self)
            displayAllEmails(self)
            displayAllPasswords(self)

            self.hide()

        def openRemoveAccountWindow():
            '''
            This is used to open the remove account window
            :return:
            '''

            from frontend.windows import RemoveAccountWindow

            RemoveAccountWindow.UIWindow.move(self.pos())
            RemoveAccountWindow.UIWindow.show()
            self.hide()



        def openViewAccountsWindow():
            '''
            This is used to open the view accounts window and adds the data to the lists
            :return:
            '''

            from frontend.windows import ViewAccountsWindow


            typesList = ViewAccountsWindow.UIWindow.typesList
            emailsList = ViewAccountsWindow.UIWindow.emailsList
            passwordsList = ViewAccountsWindow.UIWindow.passwordsList

            connection = connectToDB(self)
            cursor = connection.cursor()

            typesQuery = "SELECT AccountType FROM Accounts"
            emailsQuery = "SELECT AccountEmail FROM Accounts"
            passwordsQuery = "SELECT AccountPassword FROM Accounts"

            cursor.execute(typesQuery)
            types = cursor.fetchall()

            cursor.execute(emailsQuery)
            emails = cursor.fetchall()

            cursor.execute(passwordsQuery)
            passwords = cursor.fetchall()

            typesList.clear()
            emailsList.clear()
            passwordsList.clear()

            for type in types:
                item = QListWidgetItem(type[0])
                typesList.addItem(item)

            for email in emails:
                item = QListWidgetItem(email[0])
                emailsList.addItem(item)

            for password in passwords:
                item = QListWidgetItem(password[0])
                passwordsList.addItem(item)

            ViewAccountsWindow.UIWindow.move(self.pos())
            ViewAccountsWindow.UIWindow.show()
            self.hide()



        def openInfoDialog():
            '''
            This is used to open the info dialog
            :return:
            '''

            from frontend.windows import InfoDialog

            InfoDialog.UIDialog.move(self.pos())
            InfoDialog.UIDialog.show()
            self.hide()


        # Apply functions to/style widgets
        self.addAccountBtn.clicked.connect(openAddAccountWindow)
        self.removeAccountBtn.clicked.connect(openRemoveAccountWindow)
        self.viewAccountsBtn.clicked.connect(openViewAccountsWindow)
        self.exitCloseBtn.clicked.connect(exitApp)
        self.infoBtn.clicked.connect(openInfoDialog)


        # Displaying result of program detection
        display_success_error_label(self)

        # Connecting to database
        # connectCursor = connectToDB(self).cursor()


        # Show the app
        self.show()

    def closeEvent(self, event):
        '''
        This is used to close the window on the red X
        :param event:
        :return:
        '''

        closeConnectionToDB(self)
        sys.exit()


# initializing app

def main():
    app = QApplication(sys.argv)
    UIWindow = StartWindow()
    UIWindow.show()
    app.exec_()
