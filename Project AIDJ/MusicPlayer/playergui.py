# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MusicPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(742, 556)
        SplashScreen.setMouseTracking(True)
        SplashScreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBarBase = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(10, 10, 721, 320))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 701, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
"    border-radius:150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(85, 170, 255, 0), stop:0.75 rgba(85, 170, 255, 255));\n"
"\n"
"}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.container = QtWidgets.QFrame(self.circularProgress)
        self.container.setGeometry(QtCore.QRect(10, 10, 681, 280))
        self.container.setStyleSheet("QFrame{\n"
"border-radius:140px;\n"
"background-color: rgb(85, 85, 127);\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.label = QtWidgets.QLabel(self.container)
        self.label.setGeometry(QtCore.QRect(280, 17, 120, 21))
        font = QtGui.QFont()
        font.setFamily("Raleway Medium")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:none;\n"
"color:#FFFFFF;\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stop1 = QtWidgets.QPushButton(self.container)
        self.stop1.setGeometry(QtCore.QRect(175, 200, 41, 28))
        self.stop1.setObjectName("stop1")
        self.timestretch2 = QtWidgets.QSlider(self.container)
        self.timestretch2.setGeometry(QtCore.QRect(610, 63, 22, 160))
        self.timestretch2.setOrientation(QtCore.Qt.Vertical)
        self.timestretch2.setObjectName("timestretch2")
        self.play1 = QtWidgets.QPushButton(self.container)
        self.play1.setGeometry(QtCore.QRect(130, 200, 41, 28))
        self.play1.setObjectName("play1")
        self.songList = QtWidgets.QListView(self.container)
        self.songList.setGeometry(QtCore.QRect(130, 60, 174, 131))
        self.songList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.songList.setObjectName("songList")
        self.volume2 = QtWidgets.QSlider(self.container)
        self.volume2.setGeometry(QtCore.QRect(580, 63, 22, 160))
        self.volume2.setOrientation(QtCore.Qt.Vertical)
        self.volume2.setObjectName("volume2")
        self.forward1 = QtWidgets.QPushButton(self.container)
        self.forward1.setGeometry(QtCore.QRect(265, 200, 41, 28))
        self.forward1.setObjectName("forward1")
        self.backward1 = QtWidgets.QPushButton(self.container)
        self.backward1.setGeometry(QtCore.QRect(220, 200, 41, 28))
        self.backward1.setObjectName("backward1")
        self.songList2 = QtWidgets.QListView(self.container)
        self.songList2.setGeometry(QtCore.QRect(386, 60, 174, 131))
        self.songList2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.songList2.setObjectName("songList2")
        self.timestretch1 = QtWidgets.QSlider(self.container)
        self.timestretch1.setGeometry(QtCore.QRect(90, 63, 22, 160))
        self.timestretch1.setOrientation(QtCore.Qt.Vertical)
        self.timestretch1.setObjectName("timestretch1")
        self.volume1 = QtWidgets.QSlider(self.container)
        self.volume1.setGeometry(QtCore.QRect(60, 63, 22, 160))
        self.volume1.setOrientation(QtCore.Qt.Vertical)
        self.volume1.setObjectName("volume1")
        self.forward2 = QtWidgets.QPushButton(self.container)
        self.forward2.setGeometry(QtCore.QRect(520, 200, 41, 28))
        self.forward2.setObjectName("forward2")
        self.play2 = QtWidgets.QPushButton(self.container)
        self.play2.setGeometry(QtCore.QRect(385, 200, 41, 28))
        self.play2.setObjectName("play2")
        self.backward2 = QtWidgets.QPushButton(self.container)
        self.backward2.setGeometry(QtCore.QRect(475, 200, 41, 28))
        self.backward2.setObjectName("backward2")
        self.stop2 = QtWidgets.QPushButton(self.container)
        self.stop2.setGeometry(QtCore.QRect(430, 200, 41, 28))
        self.stop2.setObjectName("stop2")
        self.addFile = QtWidgets.QPushButton(self.container)
        self.addFile.setGeometry(QtCore.QRect(310, 110, 71, 28))
        self.addFile.setObjectName("addFile")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 701, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
"border-radius : 150px;\n"
"background-color: rgba(85, 85, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.circularBg.raise_()
        self.circularProgress.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)
        self.play1.setIcon(QtGui.QIcon("play.png"))
        self.play2.setIcon(QtGui.QIcon("play.png"))
        self.forward1.setIcon(QtGui.QIcon("forward.png"))
        self.forward2.setIcon(QtGui.QIcon("forward.png"))
        self.backward1.setIcon(QtGui.QIcon("backward.png"))
        self.backward2.setIcon(QtGui.QIcon("backward.png"))
        self.stop1.setIcon(QtGui.QIcon("stop.png"))
        self.stop2.setIcon(QtGui.QIcon("stop.png"))
        

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ababff;\">Music </span><span style=\" font-size:10pt;\">Player</span></p><p><br/></p></body></html>"))
        # self.stop1.setText(_translate("SplashScreen", "Stop"))
        # # self.play1.setText(_translate("SplashScreen", "Play"))
        # self.forward1.setText(_translate("SplashScreen", "Forward"))
        # self.backward1.setText(_translate("SplashScreen", "Backward"))
        # self.forward2.setText(_translate("SplashScreen", "Forward"))
        # self.play2.setText(_translate("SplashScreen", "Play"))
        # self.backward2.setText(_translate("SplashScreen", "Backward"))
        # self.stop2.setText(_translate("SplashScreen", "Stop"))
        self.addFile.setText(_translate("SplashScreen", "Add File"))

