
import pyodbc

def connectToDB():
    '''
    This is used to connect to the database
    :return: connect
    '''

    connectionString = 'Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=AccountGuard_PyQt5;Trusted_Connection=yes;'

    connect = pyodbc.connect(connectionString)

    if connect:
        print("Connected to the database.")

        return connect

    else:
        print("Not connect to the database.")

def closeConnectionToDB():
    '''
    This is used to close the connect to the database
    :return:
    '''

    connect = connectToDB()
    connect.close()

    print("Connection closed.")