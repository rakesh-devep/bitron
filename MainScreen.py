from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
import threading

from LoadingWindow import *

class DownloadThread(threading.Thread):
    def __init__(self, url, path,itag):
        threading.Thread.__init__(self)
        self.url = url
        self.path = path
        self.itag = itag

    def run(self):
        try:
            self.video = YouTube(self.url)
        except Exception as e:
            print(e)
            print("Video not found")
            return None

        self.stream = self.video.streams.get_by_itag(self.itag)
        self.stream.download(self.path)
        
class MainScreen(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 650)
        Dialog.setWindowIcon(QtGui.QIcon('images/logo.png'))
        Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 370,650))
        self.widget.setStyleSheet("background: #FF0000;\n"
"border-radius:10px;")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 150, 221, 25))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(90, 230, 112, 23))
        self.radioButton.setStyleSheet("color:white;")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(90, 320, 112, 23))
        self.radioButton_3.setStyleSheet("color:white;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 290, 112, 23))
        self.radioButton_2.setStyleSheet("color:white;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_1.setGeometry(QtCore.QRect(90, 260, 112, 23))
        self.radioButton_1.setStyleSheet("color:white;")
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setGeometry(QtCore.QRect(90, 350, 112, 23))
        self.radioButton_4.setStyleSheet("color:white;")
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(140, 500, 89, 31))
        self.pushButton.setStyleSheet("width: 103px;\n"
"height: 34px;\n"
"left: 128px;\n"
"top: 588px;\n"
"\n"
"background: #FFFFFF;\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.downlaod)

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(100, 20, 201, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/Logo1.png"))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(40, 120, 291, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/Url.png"))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 400, 311, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/Path.png"))
        self.label_6.setObjectName("label_6")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 430, 201, 25))
        self.lineEdit_2.setStyleSheet("background-color:white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.lineEdit_2.raise_()
        self.label_5.raise_()
        self.lineEdit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bitron"))
        Dialog.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Paste the url"))
        self.radioButton.setText(_translate("Dialog", "144p"))
        self.pushButton.setText(_translate("Dialog", "Download"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Path to save"))
        self.radioButton_3.setText(_translate("Dialog", "720p"))
        self.radioButton_2.setText(_translate("Dialog", "360p"))
        self.radioButton_1.setText(_translate("Dialog", "240p"))
        self.radioButton_4.setText(_translate("Dialog", "1080p"))

    def downlaod(self):
        self.url = self.lineEdit.text()
        self.path = self.lineEdit_2.text()
        self.itag = 18
        
        if self.radioButton.isChecked():
            self.itag = 160
        elif self.radioButton_1.isChecked():
            self.itag = 133
        elif self.radioButton_2.isChecked():
            self.itag = 18
        elif self.radioButton_3.isChecked():
            self.itag = 22
        elif self.radioButton_4.isChecked():
            self.itag = 137
        else:
            self.itag = 18
        DownloadThread(self.url,self.path,self.itag).start()


####################
#160 - 144p
#133 - 240p
#18 - 360p
#22 - 720p
#137 - 1080p
####################