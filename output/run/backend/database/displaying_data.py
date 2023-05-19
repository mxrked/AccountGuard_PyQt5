
from backend.database.accessing_db import connectToDB

def displayAllAccounts(self):
    '''
    This is used to display all the current accounts
    :return:
    '''

    connection = connectToDB(self)
    cursor = connection.cursor()

    try:

        query = "SELECT * FROM Accounts"

        cursor.execute(query)
        entries = cursor.fetchall()
        connection.commit()

        print("All Accounts:")
        for entry in entries:
            print(entry)

    except Exception as e:
        print("Error retrieving indexes. Might be that there are no indexes.")

def displayAllTypes(self):
    '''
    This is used to display all the account types
    :return:
    '''

    connection = connectToDB(self)
    cursor = connection.cursor()

    try:

        query = "SELECT AccountType FROM Accounts"

        cursor.execute(query)
        entries = cursor.fetchall()
        connection.commit()

        print("All Account Types:")
        for entry in entries:
            print(entry)

    except Exception as e:
        print("Error retrieving indexes. Might be that there are no indexes.")

def displayAllEmails(self):
    '''
    This is used to display all the account emails
    :return:
    '''

    connection = connectToDB(self)
    cursor = connection.cursor()

    try:

        query = "SELECT AccountEmail FROM Accounts"

        cursor.execute(query)
        entries = cursor.fetchall()
        connection.commit()

        print("All Account Emails:")
        for entry in entries:
            print(entry)

    except Exception as e:
        print("Error retrieving indexes. Might be that there are no indexes.")

def displayAllPasswords(self):
    '''
    This is used to display all the account passwords
    :return:
    '''

    connection = connectToDB(self)
    cursor = connection.cursor()

    try:

        query = "SELECT AccountPassword FROM Accounts"

        cursor.execute(query)
        entries = cursor.fetchall()
        connection.commit()

        print("All Account Passwords:")
        for entry in entries:
            print(entry)

    except Exception as e:
        print("Error retrieving indexes. Might be that there are no indexes.")