

from frontend.assets.funcs.detect_required_programs import check_for_required_programs

def disableBtns(self):
    '''
    This is used to disable the buttons
    :param self:
    :return:
    '''

    self.addAccountBtn.setEnabled(False)
    self.addAccountBtn.setStyleSheet("QPushButton { background-color: rgba(121, 182, 0, 0.3); border-image: none; border: none; color: rgba(0,0,0,0.4); }")
    self.removeAccountBtn.setEnabled(False)
    self.removeAccountBtn.setStyleSheet("QPushButton { background-color: rgba(121, 182, 0, 0.3); border-image: none; border: none; color: rgba(0,0,0,0.4); }")
    self.viewAccountsBtn.setEnabled(False)
    self.viewAccountsBtn.setStyleSheet("QPushButton { background-color: rgba(121, 182, 0, 0.3); border-image: none; border: none; color: rgba(0,0,0,0.4); }")

def display_success_error_label(self):
    '''
    This is used to display a specific label based on certain criteas
    :param self:
    :return:
    '''

    # Error label(s)
    if (check_for_required_programs == "SSMS was not found"):
        disableBtns(self)
        self.sSMSNotDetectedLabel.setFixedHeight(50)

    if (check_for_required_programs == "ODBC was not found"):
        disableBtns(self)
        self.oDBCNotDetectedLabel.setFixedHeight(50)

    if (check_for_required_programs == "Both programs were not found"):
        disableBtns(self)
        self.bothNotDetectedLabel.setFixedHeight(50)

    # Success label
    if (check_for_required_programs == "Both programs were found"):
        self.bothDetectedLabel.setFixedHeight(50)