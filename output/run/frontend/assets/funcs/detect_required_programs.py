
from backend.database.accessing_db import connectToDB

import pyodbc
import os

# Contents from sample_code
def find_ssms_installation_location():
    '''
    This is used to detect if the user has SSMS installed on their computer
    :return: location
    '''

    possible_locations = [
        r"C:\Program Files\Microsoft SQL Server Management Studio 19\Common7\IDE",
        r"C:\Program Files (x86)\Microsoft SQL Server Management Studio 19\Common7\IDE",
        r"D:\Microsoft SQL Server Management Studio 19\Common7\IDE",
        # Add more possible locations if applicable
    ]

    # Checking all of the locations at the top to see if that path exists
    for location in possible_locations:
        if os.path.exists(location):
            return location

    return None  # SSMS not found
def locating_odbc_drivers():
    '''
    This is used to check if ODBC Drivers are installed
    :return: boolean
    '''

    driver_name = "ODBC Driver 17 for SQL Server"
    drivers = [driver for driver in pyodbc.drivers() if driver == driver_name] # Goes through all the drivers to find one that matches the driver name
    return bool(drivers)
def checking_database_and_table(self):
    '''
    This is used to check if both the database "AccountGuard_PyQt5" and table "Accounts" exist
    :return: boolean
    '''

    connection = connectToDB(self)
    cursor = connection.cursor()

    # Checking if database exist
    checkDBQuery = "SELECT COUNT(*) FROM sys.databases WHERE name = 'AccountGuard_PyQt5'"
    cursor.execute(checkDBQuery)
    database_exists = cursor.fetchone()[0]

    if database_exists:
        foundDB = True
    else:
        foundDB = False


    checkTableQuery = "SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'Accounts'"
    cursor.execute(checkTableQuery)
    table_exists = cursor.fetchone()[0]

    if table_exists:
        foundTable = True
    else:
        foundTable = False


    if foundDB and foundTable:
        return True

    else:
        return False

# Calls for checkers
detect_odbc_drivers = locating_odbc_drivers()
ssms_installation_location = find_ssms_installation_location()

# Original content
def detect_required_programs(self):
    '''
    This will check if both programs are installed and will return its respected value
    :return: bothFound
    '''

    # foundODBC = False
    # foundSSMS = False
    # bothFound = False

    detect_db_and_table = checking_database_and_table(self) # This is used to check if both the database and table exist

    # Detect/Find SSMS
    if ssms_installation_location:
        foundSSMS = True
        print("SSMS Was Found: " + ssms_installation_location)
    else:
        foundSSMS = False

    # Detect/Find ODBC
    if detect_odbc_drivers:
        foundODBC = True
        print("Appropriate drivers detected!")
    else:
        foundODBC = False

    # Checking for database and table
    if checking_database_and_table:
        print("AccountGuard_PyQt5 exists!")

    else:
        print("AccountGuard_PyQt5 does NOT exists..")

    # Error handling
    if foundSSMS != True:
        print("SSMS WAS NOT FOUND! Use the README.md to learn where to download SSMS to.")
        sSMSNotFound = "SSMS was not found"
        return sSMSNotFound

    if foundODBC != True:
        print("ODBC Driver 17 for SQL Server WAS NOT FOUND! Install it and re-run.")
        oDBCNotFound = "ODBC was not found"
        return oDBCNotFound

    if foundSSMS != True and foundODBC != True:
        bothNotFound = "Both programs were not found"
        return bothNotFound

    # Return if both are found
    if foundSSMS and foundODBC:
        if detect_db_and_table:
            allFound = "All requirements were found"

        else:
            allFound = "Only SSMS and Drivers were found, not database and table."

        return allFound


