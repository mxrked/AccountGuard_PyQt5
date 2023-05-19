'''

    This is the Info Dialog

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.assets.qrc import app_icon

import sys


class InfoDialog(QDialog):
    def __init__(self):
        super(InfoDialog, self).__init__()

        uic.loadUi("frontend/ui/InfoDialog.ui", self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.backBtn = self.findChild(QPushButton, "infoDialog_BackBtn")
        self.linkLabel = self.findChild(QLabel, "infoDialog_LinkLabel")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def goBack():
            '''
            This is used to go back to the start window
            :return:
            '''

            from frontend.windows.StartWindow import StartWindow

            startWindow = StartWindow()
            startWindow.move(self.pos())
            startWindow.show()

            self.hide()

        def openLink():
            '''
            This is used to open the link
            :return:
            '''

            QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/mxrked/AccountGuard_PyQt5"))


        # Apply functions to/style widgets
        self.backBtn.clicked.connect(goBack)
        self.linkLabel.mousePressEvent = lambda event: openLink()


        # Show the app
        self.show()

    def closeEvent(self, event):
        '''
        This is used to close the window on the red X and reopens the start window
        :param event:
        :return:
        '''

        from frontend.windows.StartWindow import StartWindow

        startWindow = StartWindow()
        startWindow.move(self.pos())
        startWindow.show()

        self.hide()

# initializing app
app = QApplication(sys.argv)
UIDialog = InfoDialog()
app.exec_()