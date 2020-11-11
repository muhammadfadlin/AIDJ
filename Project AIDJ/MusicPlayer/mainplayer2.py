from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import playergui2,sys,time,threading
from mutagen.mp3 import MP3                             
from pygame import mixer
import pyglet



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
        self.threadStart1 = False
        self.threadStart2 = False
        self.pauseState1 = False
        self.pauseState2 = False
        self.playedAlready1 = False
        self.playedAlready2 = False
        self.index1 = 0
        self.index2 = 0
        self.playlist1 = []
        self.playlist2 = []
        self.ui.volume1.setValue(100)
        self.ui.volume1.setRange(0, 100)
        self.ui.songLengthSlider1.setValue(0)
        self.ui.volume2.setValue(100)
        self.ui.volume2.setRange(0, 100)
        self.ui.songLengthSlider2.setValue(0)

        self.ui.timestretch1.setValue(100)
        self.ui.timestretch1.setRange(0, 300)
        self.ui.timestretch2.setValue(100)
        self.ui.timestretch2.setRange(0, 300)

        self.t1 = threading.Thread(target=self.countCurrentTime1)
        self.t2 = threading.Thread(target=self.countCurrentTime2)
        
        #Connector 
        self.ui.addFile.clicked.connect(self.addFile)
        self.ui.play1.clicked.connect(self.playSong1)
        self.ui.stop1.clicked.connect(self.stopSong1)
        self.ui.backward1.clicked.connect(self.rewindSong1)
        self.ui.forward1.clicked.connect(self.nextSong1)
        self.ui.songList.itemSelectionChanged.connect(self.songDetails1)
        self.ui.volume1.valueChanged.connect(self.setVolume1)
        self.ui.songLengthSlider1.sliderPressed.connect(self.songSlider1Pressed)
        self.ui.timestretch1.valueChanged.connect(self.setTimestretch1)
        
        self.ui.play2.clicked.connect(self.playSong2)
        self.ui.stop2.clicked.connect(self.stopSong2)
        self.ui.backward2.clicked.connect(self.rewindSong2)
        self.ui.forward2.clicked.connect(self.nextSong2)
        self.ui.songList2.itemSelectionChanged.connect(self.songDetails2)
        self.ui.volume2.valueChanged.connect(self.setVolume2)
        self.ui.songLengthSlider2.sliderPressed.connect(self.songSlider2Pressed)
        self.ui.timestretch2.valueChanged.connect(self.setTimestretch2)
        
        # print(self.player1)
        pyglet.app.run()
        sys.exit(app.exec_())

    def setTimestretch1(self):
        self.player1.pitch = (self.ui.timestretch1.value() / 100)
        
    def setTimestretch2(self):
        self.player2.pitch = (self.ui.timestretch2.value() / 100)

    def songSlider1Pressed(self):
        self.pauseSong1()
        self.ui.songLengthSlider1.sliderReleased.connect(self.setSongSlider1)
        
    def songSlider2Pressed(self):
        self.pauseSong2()
        self.ui.songLengthSlider2.sliderReleased.connect(self.setSongSlider2)

    def setSongSlider1(self):
        min1,sec1 = divmod(self.ui.songLengthSlider1.value(), 60)
        self.x1 = self.ui.songLengthSlider1.value()
        print(self.x1)
        min1 = round(min1)
        sec1 = round(sec1)
        currentTime1 = '{:02d}:{:02d}'.format(min1,sec1)
        self.ui.songLength1.setText(currentTime1)
        self.player1.seek(self.x1)
        self.unpauseSong1()

    def setSongSlider2(self):
        min2,sec2 = divmod(self.ui.songLengthSlider2.value(), 60)
        self.x2 = self.ui.songLengthSlider2.value()
        print(self.x2)
        min2 = round(min2)
        sec2 = round(sec2)
        currentTime2 = '{:02d}:{:02d}'.format(min2,sec2)
        self.ui.songLength2.setText(currentTime2)
        self.player2.seek(self.x2)
        self.unpauseSong2()

    def songDetails1(self,index=None):
        if (index == None):
            self.playNow1 = self.playlist1[[x.row() for x in self.ui.songList.selectedIndexes()][0]]
            print([x.row() for x in self.ui.songList.selectedIndexes()][0])
        else:
            self.playNow1 = self.playlist1[index]
            self.ui.songList.setCurrentRow(index)
        
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
            
        # self.stopSong1()  

    def songDetails2(self,index=None):
        if (index == None):
            self.playNow2 = self.playlist2[[x.row() for x in self.ui.songList2.selectedIndexes()][0]]
            print([x.row() for x in self.ui.songList2.selectedIndexes()][0])
        else:
            self.playNow2 = self.playlist2[index]
            self.ui.songList2.setCurrentRow(index)
        
        print(self.playNow2)

        tempName2 = QUrl.fromLocalFile(self.playNow2)
        self.songName2,self.songFormat2= tempName2.fileName().rsplit('.',1)
        self.ui.songPlayed2.setText(self.songName2)
            
        if(self.songFormat2 == 'mp3'):
            tempLength2 = MP3(self.playNow2)
            self.songLength2 = tempLength2.info.length
        else:
            tempLength2 = mixer.Sound(self.playNow2)
            self.songLength2 = tempLength2.get_length()

        # self.stopSong2()  

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
    
    def addToPlaylist2(self,f):
        self.totalSong2 = len(f[0])
        for i in range(len(f[0])):
            tempSongname = QUrl.fromLocalFile(f[0][i])
            tempSongname,_ = tempSongname.fileName().rsplit('.',1)
            self.ui.songList2.insertItem(self.index2, tempSongname)
            self.playlist2.insert(self.index2,f[0][i])
            print(self.playlist2)
            self.index2 +=1
            self.totalSong2 -=1

    def countCurrentTime1(self):
        self.x1 = 0
        while self.x1 <= int(self.songLength1):
            if(self.pauseState1 == True):
                self.curMin1,self.curSec1 = divmod(self.x1, 60)
                self.curMin1 = round(self.curMin1)
                self.curSec1 = round(self.curSec1)
                self.currentTime1 = '{:02d}:{:02d}'.format(self.curMin1,self.curSec1)
                self.ui.songLength1.setText(self.currentTime1)
                print("CurrentTime Song1:",self.x1)
                self.ui.songLengthSlider1.setValue(self.x1)
                self.ui.songLengthSlider1.setRange(0,self.songLength1)
                time.sleep(1)
                self.x1 += 1
                print(int(self.songLength1))
            else:
                continue
            
            if(self.x1 >= self.songLength1):
                self.nextSong1()
            
        print("threadnya nyala pak?",self.t1.is_alive)
        
    
    def countCurrentTime2(self):
        self.x2 = 0
        while self.x2 <= self.songLength2:
            if(self.pauseState2 == True):
                self.curMin2,self.curSec2 = divmod(self.x2, 60)
                self.curMin2 = round(self.curMin2)
                self.curSec2 = round(self.curSec2)
                self.currentTime2 = '{:02d}:{:02d}'.format(self.curMin2,self.curSec2)
                self.ui.songLength2.setText(self.currentTime2)
                print("CurrentTime Song2:",self.x2)
                self.ui.songLengthSlider2.setValue(self.x2)
                self.ui.songLengthSlider2.setRange(0,self.songLength2)
                time.sleep(1)
                self.x2 += 1
            else:
                continue

    def addFile(self):
        filter = "MP3 (*.mp3);;WAV (*.wav)"
        self.file = QtWidgets.QFileDialog()
        self.file.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        self.filename = QtWidgets.QFileDialog.getOpenFileNames(filter=filter)
        self.addToPlaylist1(self.filename)
        self.addToPlaylist2(self.filename)

    def playSong1(self):
        if(not self.pauseState1):
            if(not self.playedAlready1):
                try:
                    self.player1 = pyglet.media.Player()
                    self.source1 = pyglet.media.load(self.playNow1)
                    self.player1.queue(self.source1)
                    self.player1.play()
                    self.playedAlready1 = True
                    self.pauseState1 = True
                    self.ui.play1.setIcon(QtGui.QIcon("pause.png"))
                    if(not self.threadStart1):
                        self.threadStart1 = True
                        self.t1.start()
                    
                    print("play")
                except:
                    error_dialog = QtWidgets.QErrorMessage()
                    error_dialog.showMessage('Choose A Song First')
                    error_dialog.exec_()
            else:   
                self.unpauseSong1()
        else:
            self.pauseSong1()
        print("pausestate",self.pauseState1,"playedalready",self.playedAlready1)

    def playSong2(self):
        if(not self.pauseState2):
            if(not self.playedAlready2):
                try:
                    self.player2 = pyglet.media.Player()
                    self.source2 = pyglet.media.load(self.playNow2)
                    self.player2.queue(self.source2)
                    self.player2.play()
                    self.playedAlready2 = True
                    self.pauseState2 = True
                    self.ui.play2.setIcon(QtGui.QIcon("pause.png"))
                    if(not self.threadStart2):
                        self.threadStart2 = True
                        self.t2.start()
                    print("play")
                except:
                    error_dialog = QtWidgets.QErrorMessage()
                    error_dialog.showMessage('Choose A Song First')
                    error_dialog.exec_()
            else:   
                self.unpauseSong2()
        else:
            self.pauseSong2()
        print("pausestate",self.pauseState2,"playedalready",self.playedAlready2)

    def pauseSong1(self):
        self.player1.pause()
        self.ui.play1.setIcon(QtGui.QIcon("play.png"))
        print("paused")
        self.pauseState1 = False

    def pauseSong2(self):
        self.player2.pause()
        self.ui.play2.setIcon(QtGui.QIcon("play.png"))
        print("paused")
        self.pauseState2 = False

    def unpauseSong1(self):
        self.player1.play()
        self.pauseState1 = True
        print("unpause")
        self.ui.play1.setIcon(QtGui.QIcon("pause.png"))

    def unpauseSong2(self):
        self.player2.play()
        self.pauseState2 = True
        print("unpause")
        self.ui.play2.setIcon(QtGui.QIcon("pause.png"))
        
    def stopSong1(self):      
        self.player1.pause()
        self.player1.seek(0)
        self.playedAlready1 = False   
        self.pauseState1 = False
        self.length1 = '00:00'
        self.x1 = 0
        self.ui.songLengthSlider1.setValue(0)
        self.ui.songLength1.setText(self.length1)  
        self.ui.play1.setIcon(QtGui.QIcon("play.png")) 

    def stopSong2(self):  
        self.player2.pause()
        self.player2.seek(0)
        self.playedAlready2 = False   
        self.pauseState2 = False
        self.length2 = '00:00'
        self.x2 = 0
        self.ui.songLengthSlider2.setValue(0)
        self.ui.songLength2.setText(self.length2)  
        self.ui.play2.setIcon(QtGui.QIcon("play.png"))

    def setVolume1(self):
        self.player1.volume = (self.ui.volume1.value() / 100)

    def setVolume2(self):
        self.player2.volume = (self.ui.volume2.value() / 100)

    def rewindSong1(self):
        if(self.x1 < 5 and ([x.row() for x in self.ui.songList.selectedIndexes()][0]) != 0):
            self.songDetails1([x.row() for x in self.ui.songList.selectedIndexes()][0]-1)
            self.stopSong1()
            self.playSong1()
        else:
            self.stopSong1()
            self.playSong1()

    def rewindSong2(self):
        if(self.x2 < 5 and ([x.row() for x in self.ui.songList2.selectedIndexes()][0]) != 0):
            self.songDetails2([x.row() for x in self.ui.songList2.selectedIndexes()][0]-1)
            self.stopSong1()
            self.playSong2()
        else:
            self.stopSong2()
            self.playSong2()

    def nextSong1(self):
        print(self.index1, [x.row() for x in self.ui.songList.selectedIndexes()][0])
        if(([x.row() for x in self.ui.songList.selectedIndexes()][0]) != self.index1-1):
            self.songDetails1([x.row() for x in self.ui.songList.selectedIndexes()][0]+1)
            self.stopSong1()
            self.playSong1()
        else:
            self.stopSong1()
            self.playSong1()     

    def nextSong2(self):
        print(self.index2, [x.row() for x in self.ui.songList2.selectedIndexes()][0])
        if(([x.row() for x in self.ui.songList2.selectedIndexes()][0]) != self.index1-1):
            self.songDetails2([x.row() for x in self.ui.songList2.selectedIndexes()][0]+1)
            self.stopSong1()
            self.playSong2()
        else:
            self.stopSong2()
            self.playSong2()        
 
if __name__ == "__main__":
        play = MusicPlayer()
        play.start()
        print("nyampe sini")
        
        
        