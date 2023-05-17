'''

    This is used to detect and make sure both a ODBC Driver and SSMS is installed

'''

from frontend.assets.sample_code.locating_odbc_drivers import detect_odbc_drivers
from frontend.assets.sample_code.locating_ssms import ssms_installation_location

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