from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(344, 337)
        SplashScreen.setMouseTracking(True)
        SplashScreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBarBase = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
"    border-radius:150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(85, 170, 255, 0), stop:0.75 rgba(85, 170, 255, 255));\n"
"\n"
"}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
"border-radius : 150px;\n"
"background-color: rgba(85, 85, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)
        self.container.setGeometry(QtCore.QRect(20, 20, 280, 280))
        self.container.setStyleSheet("QFrame{\n"
"border-radius:140px;\n"
"background-color: rgb(85, 85, 127);\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.label = QtWidgets.QLabel(self.container)
        self.label.setGeometry(QtCore.QRect(81, 60, 120, 16))
        font = QtGui.QFont()
        font.setFamily("Raleway Light")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:none;\n"
"color:#FFFFFF;\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.container)
        self.label_2.setGeometry(QtCore.QRect(80, 103, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color : #FFFFFF;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.container) 
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 127);color:#FFFFFF;")
        self.pushButton.setGeometry(QtCore.QRect(94, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ababff;\">BPM</span><span style=\" font-size:10pt;\"> Detector</span></p></body></html>"))
        self.label_2.setText(_translate("SplashScreen", "0"))
        self.pushButton.setText(_translate("SplashScreen", "Choose File"))


