'''

    This is the Remove Account Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from backend.database.accessing_db import connectToDB, closeConnectionToDB


import sys, re


class RemoveAccountWindow(QMainWindow):
    def __init__(self):
        super(RemoveAccountWindow, self).__init__()

        uic.loadUi("frontend/ui/RemoveAccountWindow.ui", self)

        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.backBtn = self.findChild(QPushButton, "removeAccountWindow_BackBtn")
        self.accountTypeLE = self.findChild(QLineEdit, "removeAccountWindow_AccountTypeLE")
        self.accountEmailLE = self.findChild(QLineEdit, "removeAccountWindow_AccountEmailLE")
        self.accountPasswordLE = self.findChild(QLineEdit, "removeAccountWindow_AccountPasswordLE")
        self.accountConfirmPasswordLE = self.findChild(QLineEdit, "removeAccountWindow_AccountConfirmPasswordLE")
        self.removeAccountBtn = self.findChild(QPushButton, "removeAccountWindow_RemoveAccountBtn")
        self.clearInputsBtn = self.findChild(QPushButton, "removeAccountWindow_ClearInputsBtn")
        self.accountNotExistLabel = self.findChild(QLabel, "removeAccountWindow_AccountNotExistLabel")
        self.accountRemovedLabel = self.findChild(QLabel, "removeAccountWindow_RemovedSuccessfullyLabel")
        self.errorEmptyInputsLabel = self.findChild(QLabel, "removeAccountWindow_EmptyFieldsErrorLabel")
        self.errorSpaceStartLabel = self.findChild(QLabel, "removeAccountWindow_InputsCannotStartWithSpaceLabel")
        self.errorInvalidEmailLabel = self.findChild(QLabel, "removeAccountWindow_InvalidEmailLabel")
        self.errorPasswordsNotMatchLabel = self.findChild(QLabel, "removeAccountWindow_PasswordsNotMatchLabel")

        # Define functions
        # EX: def doSomething():
        #       print("Test")
        def hideBottomLabels():
            '''
            This is used to hide the bottom labels
            :return:
            '''

            self.accountRemovedLabel.setFixedHeight(0)
            self.accountNotExistLabel.setFixedHeight(0)
            self.errorEmptyInputsLabel.setFixedHeight(0)
            self.errorSpaceStartLabel.setFixedHeight(0)
            self.errorInvalidEmailLabel.setFixedHeight(0)
            self.errorPasswordsNotMatchLabel.setFixedHeight(0)

        def clearInputs():
            '''
            This is used to clear the inputs
            :return:
            '''

            self.accountTypeLE.setText("")
            self.accountEmailLE.setText("")
            self.accountPasswordLE.setText("")
            self.accountConfirmPasswordLE.setText("")

        def checkNonEmptyInputs():
            '''
            This is used to check if any of the inputs are empty
            :return: boolean
            '''

            typeText = self.accountTypeLE.text()
            emailText = self.accountEmailLE.text()
            passwordText = self.accountPasswordLE.text()
            confirmPasswordText = self.accountConfirmPasswordLE.text()

            # Everything is filled
            if typeText != None and typeText != "" and emailText != None and emailText != "" and passwordText != None and passwordText != "" and confirmPasswordText != None and confirmPasswordText != "":
                hideBottomLabels()

                return True

            # Not filled
            if typeText == None or typeText == "":
                hideBottomLabels()
                self.errorEmptyInputsLabel.setFixedHeight(50)

                return False

            if emailText == None or emailText == "":
                hideBottomLabels()
                self.errorEmptyInputsLabel.setFixedHeight(50)

                return False

            if passwordText == None or passwordText == "":
                hideBottomLabels()
                self.errorEmptyInputsLabel.setFixedHeight(50)

                return False

            if confirmPasswordText == None or confirmPasswordText == "":
                hideBottomLabels()
                self.errorEmptyInputsLabel.setFixedHeight(50)

                return False

        def checkPasswordsMatch():
            '''
            This is used to check if the passwords match
            :return: boolean
            '''

            passwordText = self.accountPasswordLE.text()
            confirmPasswordText = self.accountConfirmPasswordLE.text()

            if passwordText == confirmPasswordText:
                hideBottomLabels()

                return True
            else:
                hideBottomLabels()
                self.errorPasswordsNotMatchLabel.setFixedHeight(50)

                return False

        def checkForNoStartSpaces():
            '''
            This is used to check if there are any spaces for the first value in the inputs
            :return: boolean
            '''

            typeText = self.accountTypeLE.text()
            emailText = self.accountEmailLE.text()
            passwordText = self.accountPasswordLE.text()
            confirmPasswordText = self.accountConfirmPasswordLE.text()

            if not typeText.startswith(" ") and not emailText.startswith(" ") and not passwordText.startswith(" ") and not confirmPasswordText.startswith(" "):
                hideBottomLabels()

                return True
            else:
                hideBottomLabels()
                self.errorSpaceStartLabel.setFixedHeight(50)

                return False

        def checkForValidEmail():
            '''
            This is used to check if the email is a valid one
            :return:
            '''

            emailText = self.accountEmailLE.text()
            regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

            # Checking if valid/invalid
            if re.match(regex, emailText):
                hideBottomLabels()

                return True
            else:
                hideBottomLabels()
                self.errorInvalidEmailLabel.setFixedHeight(50)

                return False

        def checkAccountExist(cursor):
            '''
            This is used to check if an account exsists
            :param cursor:
            :return: boolean
            '''

            typeText = self.accountTypeLE.text()
            emailText = self.accountEmailLE.text()
            passwordText = self.accountPasswordLE.text()

            query = "SELECT COUNT(*) FROM Accounts WHERE AccountType = ? AND AccountEmail = ? AND AccountPassword = ?"
            cursor.execute(query, (typeText, emailText, passwordText))
            count = cursor.fetchone()[0] # This will grab the first one that matches

            if count > 0:
                return True
            else:
                return False

        def removeAccount():
            '''
            This is used to remove an account
            :return:
            '''

            connection = connectToDB(self)
            cursor = connection.cursor()

            # Calls for condition checks
            nonEmptyCheck = checkNonEmptyInputs()
            matchPasswordsCheck = checkPasswordsMatch()
            noSpacesCheck = checkForNoStartSpaces()
            validEmailCheck = checkForValidEmail()
            accountExists = checkAccountExist(cursor)

            typeText = self.accountTypeLE.text()
            emailText = self.accountEmailLE.text()
            passwordText = self.accountPasswordLE.text()

            # Checking for errors and conditions
            if nonEmptyCheck:

                if noSpacesCheck:

                    if matchPasswordsCheck:

                        if validEmailCheck:

                           if accountExists:

                                # Removing account
                               try:
                                   query = "DELETE FROM Accounts WHERE AccountType = ? AND AccountEmail = ? AND AccountPassword = ?"
                                   cursor.execute(query, (typeText, emailText, passwordText))
                                   connection.commit()

                                   hideBottomLabels()
                                   clearInputs()

                                   self.accountRemovedLabel.setFixedHeight(50)
                                   print("Removed account successfully!")

                               except Exception as e:
                                   print("Error inserting data:" + str(e))

                           else:

                               print("That account does not exist..")

                               hideBottomLabels()

                               self.accountNotExistLabel.setFixedHeight(50)

                        else:

                            print("The email address is not valid.")

                            hideBottomLabels()
                            self.errorInvalidEmailLabel.setFixedHeight(50)

                    else:

                        print("The passwords do not match.")

                        hideBottomLabels()
                        self.errorPasswordsNotMatchLabel.setFixedHeight(50)

                else:

                    print("Inputs cannot start with a space.")

                    hideBottomLabels()
                    self.errorSpaceStartLabel.setFixedHeight(50)

            else:

                print("One or more inputs is empty.")

                hideBottomLabels()
                self.errorEmptyInputsLabel.setFixedHeight(50)

        def goBack():
            '''
            This is used to go back to the start window
            :return:
            '''

            from frontend.windows.StartWindow import StartWindow

            clearInputs()
            hideBottomLabels()

            startWindow = StartWindow()
            startWindow.move(self.pos())
            startWindow.show()

            closeConnectionToDB(self)

            self.hide()


        # Apply functions to/style widgets
        self.backBtn.clicked.connect(goBack)
        self.removeAccountBtn.clicked.connect(removeAccount)
        self.clearInputsBtn.clicked.connect(clearInputs)


        # Show the app
        self.show()

    def closeEvent(self, event):
        '''
        This is used to close the window on the red X and reopens the start window
        :param event:
        :return:
        '''

        from frontend.windows.StartWindow import StartWindow

        self.accountTypeLE.setText("")
        self.accountEmailLE.setText("")
        self.accountPasswordLE.setText("")
        self.accountConfirmPasswordLE.setText("")
        self.accountRemovedLabel.setFixedHeight(0)
        self.accountNotExistLabel.setFixedHeight(0)
        self.errorEmptyInputsLabel.setFixedHeight(0)
        self.errorSpaceStartLabel.setFixedHeight(0)
        self.errorInvalidEmailLabel.setFixedHeight(0)
        self.errorPasswordsNotMatchLabel.setFixedHeight(0)

        startWindow = StartWindow()
        startWindow.move(self.pos())
        startWindow.show()

        closeConnectionToDB(self)

        self.hide()

# initializing app
app = QApplication(sys.argv)
UIWindow = RemoveAccountWindow()
app.exec_()