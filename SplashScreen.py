from PyQt5 import QtCore, QtGui, QtWidgets


class SplashScreen(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 650)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 370, 650))
        self.widget.setStyleSheet("background: #FF0000;\n"
"border-radius:10px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 210, 251, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Logo.png"))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bitron"))
        Dialog.setWindowIcon(QtGui.QIcon('images/logo.png'))
