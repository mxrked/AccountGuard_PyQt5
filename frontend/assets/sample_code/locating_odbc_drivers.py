'''

    This is used to check if ODBC Drivers are installed

'''

import pyodbc

def locating_odbc_drivers():

    driver_name = "ODBC Driver 17 for SQL Server"
    drivers = [driver for driver in pyodbc.drivers() if driver == driver_name] # Goes through all the drivers to find one that matches the driver name
    return bool(drivers)

detect_odbc_drivers = locating_odbc_drivers()