
import pyodbc

connect = None # This is used to pass the close function on the connection if there isnt one

def connectToDB(self):
    '''
    This is used to connect to the database
    :return: connect
    '''

    # This is used to pass the close function on the connection if there isnt one
    global connect

    try:

        # This is used to pass the close function on the connection if there isnt one
        if connect is not None:
            return connect

        connectionString = 'Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=AccountGuard_PyQt5;Trusted_Connection=yes;'
        connect = pyodbc.connect(connectionString)

        if connect:
            print("Connected to the database.")
            return connect

    except pyodbc.Error as e:

        print("Failed to/Not connect to the database.")

        # Displaying failed connection error
        self.failedToConnectLabel.setFixedHeight(50)

        # Disabling buttons
        self.addAccountBtn.setEnabled(False)
        self.addAccountBtn.setStyleSheet(
            "QPushButton { background-color: rgba(121, 182, 0, 0.3); border-image: none; border: none; color: rgba(0,0,0,0.4); }")
        self.removeAccountBtn.setEnabled(False)
        self.removeAccountBtn.setStyleSheet(
            "QPushButton { background-color: rgba(121, 182, 0, 0.3); border-image: none; border: none; color: rgba(0,0,0,0.4); }")
        self.viewAccountsBtn.setEnabled(False)
        self.viewAccountsBtn.setStyleSheet(
            "QPushButton { background-color: rgba(121, 182, 0, 0.3); border-image: none; border: none; color: rgba(0,0,0,0.4); }")

def closeConnectionToDB(self):
    '''
    This is used to close the connect to the database
    :return:
    '''

    # This is used to pass the close function on the connection if there isnt one
    global connect

    try:

        # This is used to pass the close function on the connection if there isnt one
        if connect is not None:
            connect = connectToDB(self)
            connect.close()

            connect = None

            print("Connection closed.")

    except pyodbc.Error as e:
        pass