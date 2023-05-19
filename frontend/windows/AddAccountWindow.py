'''

    This is the Add Account Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui, Qt
from PyQt5.QtGui import QCursor

from backend.database.accessing_db import connectToDB, closeConnectionToDB


import sys, re


class AddAccountWindow(QMainWindow):


    def __init__(self):
        super(AddAccountWindow, self).__init__()

        uic.loadUi("frontend/ui/AddAccountWindow.ui", self)

        # Define widgets
        self.backBtn = self.findChild(QPushButton, "addAccountWindow_BackBtn")
        self.accountTypeLE = self.findChild(QLineEdit, "addAccountWindow_AccountTypeLE")
        self.accountEmailLE = self.findChild(QLineEdit, "addAccountWindow_AccountEmailLE")
        self.accountPasswordLE = self.findChild(QLineEdit, "addAccountWindow_AccountPasswordLE")
        self.accountConfirmPasswordLE = self.findChild(QLineEdit, "addAccountWindow_AccountConfirmPasswordLE")
        self.addAccountBtn = self.findChild(QPushButton, "addAccountWindow_AddAccountBtn")
        self.clearInputsBtn = self.findChild(QPushButton, "addAccountWindow_ClearInputsBtn")
        self.successLabel = self.findChild(QLabel, "addAccountWindow_AccountAddedLabel")
        self.errorEmailTypeLabel = self.findChild(QLabel, "addAccountWindow_EmailTypeInUseLabel")
        self.errorEmptyInputsLabel = self.findChild(QLabel, "addAccountWindow_EmptyFieldsErrorLabel")
        self.errorSpaceStartLabel = self.findChild(QLabel, "addAccountWindow_InputsCannotStartWithSpaceLabel")
        self.errorInvalidEmailLabel = self.findChild(QLabel, "addAccountWindow_InvalidEmailLabel")
        self.errorPasswordsNotMatchLabel = self.findChild(QLabel, "addAccountWindow_PasswordsNotMatchLabel")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def hideBottomLabels():
            '''
            This is used to hide the bottom labels
            :return:
            '''

            self.successLabel.setFixedHeight(0)
            self.errorEmailTypeLabel.setFixedHeight(0)
            self.errorEmptyInputsLabel.setFixedHeight(0)
            self.errorSpaceStartLabel.setFixedHeight(0)
            self.errorInvalidEmailLabel.setFixedHeight(0)
            self.errorPasswordsNotMatchLabel.setFixedHeight(0)

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

        def checkAccountNotAlreadyInUse(cursor):
            '''
            This is used to check if the account being added is already in use by checking
            the type and email
            :return: boolean
            '''


            typeText = self.accountTypeLE.text()
            emailText = self.accountEmailLE.text()

            query = "SELECT COUNT(*) FROM Accounts WHERE AccountType = ? AND AccountEmail = ?"
            cursor.execute(query, (typeText, emailText))
            count = cursor.fetchone()[0] # This will grab the first one that matches

            if count > 0:
                return False # Already in use..
            else:
                return True # New account!

        def addAccount():
            '''
            This is used to add an account
            :return:
            '''

            connection = connectToDB(self)
            cursor = connection.cursor()

            # Calls for condition checks
            nonEmptyCheck = checkNonEmptyInputs()
            matchPasswordsCheck = checkPasswordsMatch()
            noSpacesCheck = checkForNoStartSpaces()
            validEmailCheck = checkForValidEmail()
            nonExsistingAccount = checkAccountNotAlreadyInUse(cursor)

            typeText = self.accountTypeLE.text()
            emailText = self.accountEmailLE.text()
            passwordText = self.accountPasswordLE.text()

            # Checking for errors and conditions
            if nonEmptyCheck:

                if noSpacesCheck:

                    if matchPasswordsCheck:

                        if validEmailCheck:

                            if nonExsistingAccount:

                                # Adding the account/creating error
                                try:

                                    connection = connectToDB(self)
                                    cursor = connection.cursor()

                                    # print(connectCursor)

                                    # Inserting account to table
                                    query = f"INSERT INTO Accounts (AccountType, AccountEmail, AccountPassword) VALUES (?, ?, ?)"

                                    print(query)

                                    cursor.execute(query, (typeText, emailText, passwordText))
                                    # cursor.execute(query)
                                    connection.commit()
                                    print("Data was inserted.")

                                    hideBottomLabels()
                                    clearInputs()
                                    self.successLabel.setFixedHeight(50)

                                except Exception as e:
                                    print("Error inserting data:" + str(e))

                            else:

                                print("That email and type is already in use.")

                                hideBottomLabels()
                                self.errorEmailTypeLabel.setFixedHeight(50)

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

        def clearInputs():
            '''
            This is used to clear the inputs
            :return:
            '''

            self.accountTypeLE.setText("")
            self.accountEmailLE.setText("")
            self.accountPasswordLE.setText("")
            self.accountConfirmPasswordLE.setText("")

        def goBack():
            '''
            This is used to go back to the start window
            :return:
            '''

            from frontend._py.StartWindow import StartWindow

            clearInputs()
            hideBottomLabels()

            startWindow = StartWindow()
            startWindow.move(self.pos())
            startWindow.show()

            closeConnectionToDB(self)

            self.hide()


        # Apply functions to/style widgets
        self.backBtn.clicked.connect(goBack)
        self.clearInputsBtn.clicked.connect(clearInputs)
        self.addAccountBtn.clicked.connect(addAccount)


        # Show the app
        self.show()



    def closeEvent(self, event):
        '''
        This is used to close the window on the red X and reopens the start window
        :param event:
        :return:
        '''

        from frontend._py.StartWindow import StartWindow

        self.accountTypeLE.setText("")
        self.accountEmailLE.setText("")
        self.accountPasswordLE.setText("")
        self.accountConfirmPasswordLE.setText("")
        self.successLabel.setFixedHeight(0)
        self.errorEmailTypeLabel.setFixedHeight(0)
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
UIWindow = AddAccountWindow()
app.exec_()