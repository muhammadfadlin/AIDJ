from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import playergui,sys
from pygame import mixer



class MusicPlayer():
    def __init__(self):
        self.pauseState1 = False
        self.playedAlready1 = False
        # print("masuksiniii")
        mixer.init()
        app = QtWidgets.QApplication(sys.argv)
        self.SplashScreen = QtWidgets.QMainWindow()
        self.ui = playergui.Ui_SplashScreen()
        self.ui.setupUi(self.SplashScreen)
        self.SplashScreen.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.SplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent
        self.SplashScreen.show()

        #Value Set
        
        self.ui.volume1.setValue(100)
        self.ui.volume1.setRange(0, 100)
        self.ui.volume1.valueChanged.connect(self.setVolume1)

        #Connector
        self.ui.addFile.clicked.connect(self.addFile)
        self.ui.play1.clicked.connect(self.playSong1)
        self.ui.stop1.clicked.connect(self.stopSong1)
        
        sys.exit(app.exec_())

    def addFile(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName()
        print(self.filename[0])

    def playSong1(self):
        if(not self.pauseState1):
            if(not self.playedAlready1):
                try:
                    mixer.music.load(self.filename[0])
                    mixer.music.play()
                    self.playedAlready1 = True
                    self.pauseState1 = True
                    self.ui.play1.setIcon(QtGui.QIcon("pause.png"))
                    print("play")
                except:
                    error_dialog = QtWidgets.QErrorMessage()
                    error_dialog.showMessage('Choose A Song First')
                    error_dialog.exec_()
            else:   
                mixer.music.unpause()
                self.pauseState1 = True
                print("unpause")
                self.ui.play1.setIcon(QtGui.QIcon("pause.png"))
        else:
            mixer.music.pause()
            self.ui.play1.setIcon(QtGui.QIcon("play.png"))
            print("paused")
            self.pauseState1 = False
            
        print("pausestate",self.pauseState1,"playedalready",self.playedAlready1)

    def stopSong1(self):
        mixer.music.stop()
        self.playedAlready1 = False
        self.pauseState1 = False
        self.ui.play1.setIcon(QtGui.QIcon("play.png")) 

    def setVolume1(self):
        mixer.music.set_volume(self.ui.volume1.value() / 100)

    # def playSong2(self):

if __name__ == "__main__":
        test = MusicPlayer()
        