import sys 
import time
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

from SplashScreen import SplashScreen
from MainScreen import MainScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = QtWidgets.QWidget()
    main = QtWidgets.QWidget()

    splashscreen = SplashScreen()
    splashscreen.setupUi(splash)
    splash.show()

    mainscreen = MainScreen()
    mainscreen.setupUi(main)

    
    QTimer.singleShot(2000, splash.close)
    QTimer.singleShot(2000, main.show)

    app.exec_()