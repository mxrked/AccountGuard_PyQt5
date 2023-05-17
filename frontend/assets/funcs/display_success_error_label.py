

from frontend.assets.funcs.detect_required_programs import check_for_required_programs

def display_success_error_label(self):
    '''
    This is used to display a specific label based on certain criteas
    :param self:
    :return:
    '''

    # Error label(s)
    if (check_for_required_programs == "SSMS was not found"):
        self.sSMSNotDetectedLabel.setFixedHeight(50)

    if (check_for_required_programs == "ODBC was not found"):
        self.oDBCNotDetectedLabel.setFixedHeight(50)

    if (check_for_required_programs == "Both programs were not found"):
        self.bothNotDetectedLabel.setFixedHeight(50)

    # Success label
    if (check_for_required_programs == "Both programs were found"):
        self.bothDetectedLabel.setFixedHeight(50)