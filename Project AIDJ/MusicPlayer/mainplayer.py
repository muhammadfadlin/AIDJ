from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import playergui2,sys,time,threading
from mutagen.mp3 import MP3                             
from pygame import mixer



class MusicPlayer():
    def __init__(self):
        mixer.init()
        app = QtWidgets.QApplication(sys.argv)
        self.SplashScreen = QtWidgets.QMainWindow()
        self.ui = playergui2.Ui_SplashScreen()
        self.ui.setupUi(self.SplashScreen)
        self.SplashScreen.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.SplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent
        self.SplashScreen.show()

        #Value Set
        self.pauseState1 = False
        self.playedAlready1 = False
        self.index1 = 0
        self.playlist1 = []
        self.ui.volume1.setValue(100)
        self.ui.volume1.setRange(0, 100)
        self.ui.volume1.valueChanged.connect(self.setVolume1)
        self.ui.songLengthSlider1.setValue(0)


        #Connector 
        self.ui.addFile.clicked.connect(self.addFile)
        self.ui.play1.clicked.connect(self.playSong1)
        self.ui.stop1.clicked.connect(self.stopSong1)
        self.ui.backward1.clicked.connect(self.rewindSong1)
        self.ui.songList.itemSelectionChanged.connect(self.songDetails1)
        sys.exit(app.exec_())

    # def prinprinan(self):
        # print(self.ui.songList.selectedIndexes()[0].row)


    def songDetails1(self):
        print([x.row() for x in self.ui.songList.selectedIndexes()][0])
        self.playNow1 = self.playlist1[[x.row() for x in self.ui.songList.selectedIndexes()][0]]
        print(self.playNow1)

        tempName1 = QUrl.fromLocalFile(self.playNow1)
        self.songName1,self.songFormat1= tempName1.fileName().rsplit('.',1)
        self.ui.songPlayed1.setText(self.songName1)
            
        if(self.songFormat1 == 'mp3'):
            tempLength1 = MP3(self.playNow1)
            self.songLength1 = tempLength1.info.length
        else:
            tempLength1 = mixer.Sound(self.playNow1)
            self.songLength1 = tempLength1.get_length()

        self.stopSong1()  

    def addToPlaylist1(self,f):
        self.totalSong1 = len(f[0])
        for i in range(len(f[0])):
            tempSongname = QUrl.fromLocalFile(f[0][i])
            tempSongname,_ = tempSongname.fileName().rsplit('.',1)
            self.ui.songList.insertItem(self.index1, tempSongname)
            self.playlist1.insert(self.index1,f[0][i])
            print(self.playlist1)
            self.index1 +=1
            self.totalSong1 -=1

    def countCurrentTime1(self,t):
        x = 0
        while x <= t and mixer.music.get_busy():
            if(self.pauseState1 == True):
                self.curMin1,self.curSec1 = divmod(x, 60)
                self.curMin1 = round(self.curMin1)
                self.curSec1 = round(self.curSec1)
                self.currentTime1 = '{:02d}:{:02d}'.format(self.curMin1,self.curSec1)
                self.ui.songLength1.setText(self.currentTime1)
                print(t)
                self.ui.songLengthSlider1.setValue(x)
                self.ui.songLengthSlider1.setRange(0,t)
                time.sleep(1)
                x += 1
            else:
                continue

    def addFile(self):
            filter = "MP3 (*.mp3);;WAV (*.wav)"
            self.file = QtWidgets.QFileDialog()
            self.file.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
            self.filename1 = QtWidgets.QFileDialog.getOpenFileNames(filter=filter)
            self.addToPlaylist1(self.filename1)

    def playSong1(self):
        if(not self.pauseState1):
            if(not self.playedAlready1):
                try:
                    mixer.music.load(self.playNow1)
                    mixer.music.play()
                    self.playedAlready1 = True
                    self.pauseState1 = True
                    self.threadDestroy1 = False
                    self.ui.play1.setIcon(QtGui.QIcon("pause.png"))
                    t1 = threading.Thread(target=self.countCurrentTime1,args=(self.songLength1,))
                    t1.start()
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
        self.length1 = '00:00'
        self.ui.songLengthSlider1.setValue(0)
        self.ui.songLength1.setText(self.length1)  
        self.ui.play1.setIcon(QtGui.QIcon("play.png")) 

    def setVolume1(self):
        mixer.music.set_volume(self.ui.volume1.value() / 100)

    def rewindSong1(self):
        self.stopSong1()
        self.playSong1()

    # def songDetails(self):
    #     self.ui.songPlayed1.setText(self.filename[0])


if __name__ == "__main__":
        play = MusicPlayer()
        
        