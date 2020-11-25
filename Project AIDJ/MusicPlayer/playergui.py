# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MusicPlayerBPM.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(865, 410)
        SplashScreen.setMouseTracking(True)
        SplashScreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBarBase = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(10, 10, 781, 341))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 731, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
"    border-radius:150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(85, 170, 255, 0), stop:0.75 rgba(85, 170, 255, 255));\n"
"\n"
"}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.container = QtWidgets.QFrame(self.circularProgress)
        self.container.setGeometry(QtCore.QRect(10, 10, 711, 291))
        self.container.setStyleSheet("QFrame{\n"
"border-radius:140px;\n"
"background-color: rgb(85, 85, 127);\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.title = QtWidgets.QLabel(self.container)
        self.title.setGeometry(QtCore.QRect(294, 14, 120, 21))
        font = QtGui.QFont()
        font.setFamily("Raleway Medium")
        self.title.setFont(font)
        self.title.setStyleSheet("background-color:none;\n"
"color:#FFFFFF;\n"
"")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.stop1 = QtWidgets.QPushButton(self.container)
        self.stop1.setGeometry(QtCore.QRect(187, 249, 41, 28))
        self.stop1.setObjectName("stop1")
        self.play1 = QtWidgets.QPushButton(self.container)
        self.play1.setGeometry(QtCore.QRect(142, 249, 41, 28))
        self.play1.setStyleSheet("")
        self.play1.setObjectName("play1")
        self.songList = QtWidgets.QListWidget(self.container)
        self.songList.setGeometry(QtCore.QRect(142, 60, 174, 131))
        self.songList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.songList.setObjectName("songList")
        self.forward1 = QtWidgets.QPushButton(self.container)
        self.forward1.setGeometry(QtCore.QRect(277, 249, 41, 28))
        self.forward1.setObjectName("forward1")
        self.backward1 = QtWidgets.QPushButton(self.container)
        self.backward1.setGeometry(QtCore.QRect(232, 249, 41, 28))
        self.backward1.setObjectName("backward1")
        self.songList2 = QtWidgets.QListWidget(self.container)
        self.songList2.setGeometry(QtCore.QRect(398, 60, 174, 131))
        self.songList2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.songList2.setObjectName("songList2")
        self.forward2 = QtWidgets.QPushButton(self.container)
        self.forward2.setGeometry(QtCore.QRect(532, 251, 41, 28))
        self.forward2.setObjectName("forward2")
        self.play2 = QtWidgets.QPushButton(self.container)
        self.play2.setGeometry(QtCore.QRect(397, 251, 41, 28))
        self.play2.setStyleSheet("")
        self.play2.setObjectName("play2")
        self.backward2 = QtWidgets.QPushButton(self.container)
        self.backward2.setGeometry(QtCore.QRect(487, 251, 41, 28))
        self.backward2.setObjectName("backward2")
        self.stop2 = QtWidgets.QPushButton(self.container)
        self.stop2.setGeometry(QtCore.QRect(442, 251, 41, 28))
        self.stop2.setObjectName("stop2")
        self.addFile = QtWidgets.QPushButton(self.container)
        self.addFile.setGeometry(QtCore.QRect(327, 110, 61, 21))
        self.addFile.setObjectName("addFile")
        self.songLengthSlider1 = QtWidgets.QSlider(self.container)
        self.songLengthSlider1.setGeometry(QtCore.QRect(142, 200, 171, 22))
        self.songLengthSlider1.setOrientation(QtCore.Qt.Horizontal)
        self.songLengthSlider1.setObjectName("songLengthSlider1")
        self.songLengthSlider2 = QtWidgets.QSlider(self.container)
        self.songLengthSlider2.setGeometry(QtCore.QRect(399, 200, 171, 22))
        self.songLengthSlider2.setOrientation(QtCore.Qt.Horizontal)
        self.songLengthSlider2.setObjectName("songLengthSlider2")
        self.songPlayed1 = QtWidgets.QLabel(self.container)
        self.songPlayed1.setGeometry(QtCore.QRect(144, 36, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        self.songPlayed1.setFont(font)
        self.songPlayed1.setStyleSheet("background-color:none;\n"
"color:#FFFFFF;\n"
"")
        self.songPlayed1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.songPlayed1.setAlignment(QtCore.Qt.AlignCenter)
        self.songPlayed1.setObjectName("songPlayed1")
        self.songLength1 = QtWidgets.QLabel(self.container)
        self.songLength1.setGeometry(QtCore.QRect(170, 220, 120, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        self.songLength1.setFont(font)
        self.songLength1.setStyleSheet("background-color:none;\n"
"color:#FFFFFF;\n"
"")
        self.songLength1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.songLength1.setAlignment(QtCore.Qt.AlignCenter)
        self.songLength1.setObjectName("songLength1")
        self.songPlayed2 = QtWidgets.QLabel(self.container)
        self.songPlayed2.setGeometry(QtCore.QRect(400, 37, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        self.songPlayed2.setFont(font)
        self.songPlayed2.setStyleSheet("background-color:none;\n"
"color:#FFFFFF;\n"
"")
        self.songPlayed2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.songPlayed2.setAlignment(QtCore.Qt.AlignCenter)
        self.songPlayed2.setObjectName("songPlayed2")
        self.songLength2 = QtWidgets.QLabel(self.container)
        self.songLength2.setGeometry(QtCore.QRect(430, 220, 120, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        self.songLength2.setFont(font)
        self.songLength2.setStyleSheet("background-color:none;\n"
"color:#FFFFFF;\n"
"")
        self.songLength2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.songLength2.setAlignment(QtCore.Qt.AlignCenter)
        self.songLength2.setObjectName("songLength2")
        self.volume1 = QtWidgets.QDial(self.container)
        self.volume1.setGeometry(QtCore.QRect(70, 60, 61, 71))
        self.volume1.setObjectName("volume1")
        self.timestretch1 = QtWidgets.QDial(self.container)
        self.timestretch1.setGeometry(QtCore.QRect(70, 120, 61, 71))
        self.timestretch1.setObjectName("timestretch1")
        self.timestretch2 = QtWidgets.QDial(self.container)
        self.timestretch2.setGeometry(QtCore.QRect(580, 120, 61, 71))
        self.timestretch2.setObjectName("timestretch2")
        self.volume2 = QtWidgets.QDial(self.container)
        self.volume2.setGeometry(QtCore.QRect(580, 60, 61, 71))
        self.volume2.setObjectName("volume2")
        self.bpm2 = QtWidgets.QLabel(self.container)
        self.bpm2.setGeometry(QtCore.QRect(639, 115, 55, 21))
        font = QtGui.QFont()
        font.setFamily("HP Simplified")
        self.bpm2.setFont(font)
        self.bpm2.setAlignment(QtCore.Qt.AlignCenter)
        self.bpm2.setObjectName("bpm2")
        self.bpm2.setStyleSheet("background-color:none;\n"
"color:#FFFFFF;\n"
"")
        self.bpm1 = QtWidgets.QLabel(self.container)
        self.bpm1.setGeometry(QtCore.QRect(18, 115, 55, 21))
        self.bpm1.setStyleSheet("background-color:none;\n"
"color:#FFFFFF;\n"
"")
        font = QtGui.QFont()
        font.setFamily("HP Simplified")
        self.bpm1.setFont(font)
        self.bpm1.setAlignment(QtCore.Qt.AlignCenter)
        self.bpm1.setObjectName("bpm1")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 731, 311))
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
        self.title.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ababff;\">AI </span><span style=\" font-size:10pt;\">DJ</span></p><p><br/></p></body></html>"))
        # self.stop1.setText(_translate("SplashScreen", "Stop"))
        # self.play1.setText(_translate("SplashScreen", "Play"))
        # self.forward1.setText(_translate("SplashScreen", "Forward"))
        # self.backward1.setText(_translate("SplashScreen", "Backward"))
        # self.forward2.setText(_translate("SplashScreen", "Forward"))
        # self.play2.setText(_translate("SplashScreen", "Play"))
        # self.backward2.setText(_translate("SplashScreen", "Backward"))
        # self.stop2.setText(_translate("SplashScreen", "Stop"))
        self.addFile.setText(_translate("SplashScreen", "Add File"))
        # self.songPlayed1.setText(_translate("SplashScreen", "<html><head/><body><p>Playing - Lagu .mp3</p></body></html>"))
        # self.songLength1.setText(_translate("SplashScreen", "<html><head/><body><p>00:00</p></body></html>"))
        # self.songPlayed2.setText(_translate("SplashScreen", "<html><head/><body><p>Playing - Lagu .mp3</p></body></html>"))
        # self.songLength2.setText(_translate("SplashScreen", "<html><head/><body><p>00:00</p></body></html>"))
        # self.bpm2.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" color:#ffffff;\">128.87</span></p></body></html>"))
        # self.bpm1.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" color:#ffffff;\">128.87</span></p></body></html>"))
