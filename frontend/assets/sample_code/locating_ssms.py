'''

    This is used to detect if the user has SSMS installed on their computer

'''

import os

def find_ssms_installation_location():
    possible_locations = [
        r"C:\Program Files\Microsoft SQL Server Management Studio 19\Common7\IDE",
        r"C:\Program Files (x86)\Microsoft SQL Server Management Studio 19\Common7\IDE",
        r"D:\Microsoft SQL Server Management Studio 19\Common7\IDE",
        # Add more possible locations if applicable
    ]

    for location in possible_locations:
        if os.path.exists(location):
            return location

    return None  # SSMS not found

ssms_installation_location = find_ssms_installation_location()