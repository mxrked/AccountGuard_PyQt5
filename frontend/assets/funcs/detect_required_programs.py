
import pyodbc
import os

# Contents from sample_code
def find_ssms_installation_location():
    '''
    This is used to detect if the user has SSMS installed on their computer
    :return:
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
    :return:
    '''

    driver_name = "ODBC Driver 17 for SQL Server"
    drivers = [driver for driver in pyodbc.drivers() if driver == driver_name] # Goes through all the drivers to find one that matches the driver name
    return bool(drivers)
detect_odbc_drivers = locating_odbc_drivers()
ssms_installation_location = find_ssms_installation_location()

# Original content
def detect_required_programs():
    '''
    This will check if both programs are installed and will return its respected value
    :return: bothFound
    '''

    # foundODBC = False
    # foundSSMS = False
    # bothFound = False

    # Detect/Find SSMS
    if (ssms_installation_location):
        foundSSMS = True
        print("SSMS Was Found: " + ssms_installation_location)
    else:
        foundSSMS = False

    # Detect/Find ODBC
    if (detect_odbc_drivers):
        foundODBC = True
        print("Appropriate drivers detected!")
    else:
        foundODBC = False


    # Error handling
    if (foundSSMS != True):
        print("SSMS WAS NOT FOUND! Use the README.md to learn where to download SSMS to.")
        sSMSNotFound = "SSMS was not found"
        return sSMSNotFound

    if (foundODBC != True):
        print("ODBC Driver 17 for SQL Server WAS NOT FOUND! Install it and re-run.")
        oDBCNotFound = "ODBC was not found"
        return oDBCNotFound

    if (foundSSMS != True and foundODBC != True):
        bothNotFound = "Both programs were not found"
        return bothNotFound

    # Return if both are found
    if (foundSSMS and foundODBC):
        bothFound = "Both programs were found"

        return bothFound
check_for_required_programs = detect_required_programs()