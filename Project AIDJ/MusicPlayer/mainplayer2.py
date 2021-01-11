#Author : Muhammad Fadli
#AI DJ Project

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl,QThread
from mutagen.mp3 import MP3
from madmom.models import BEATS_LSTM    
import pyglet
import sox
import madmom
import playergui,sys,time,threading 

class MusicPlayer():
    def __init__(self):     
        #Build User Interface Using PyQT5 
        self.app = QtWidgets.QApplication(sys.argv)
        self.SplashScreen = QtWidgets.QMainWindow()
        self.ui = playergui.Ui_SplashScreen()
        self.ui.setupUi(self.SplashScreen)
        self.SplashScreen.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.SplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent
        self.SplashScreen.show()

        #Value Set
        self.timeInterval = 0.01
        self.time1 = 0 #timer1
        self.time2 = 0 #timer2
        self.pauseState1 = True
        self.pauseState2 = True
        self.playedAlready1 = False
        self.playedAlready2 = False
        self.bpm1Changed = False
        self.bpm2Changed = False
        self.aligned1 = True
        self.aligned2 = True
        self.index = 0
        self.playlist = [[]]
        self.ui.volume1.setRange(0, 1000)
        self.ui.volume1.setValue(1000)
        self.ui.songLengthSlider1.setValue(0)
        self.ui.volume2.setRange(0, 1000)
        self.ui.volume2.setValue(1000)
        self.ui.songLengthSlider2.setValue(0)
        
        self.ui.timestretch1.setRange(50000, 150000) #Pitch of 0 is not permitted based on the library
        self.ui.timestretch1.setValue(100000)
        self.ui.timestretch2.setRange(50000, 150000)
        self.ui.timestretch2.setValue(100000)
        
        #Prepare 2 different players 
        self.player2 = pyglet.media.Player()
        self.player1 = pyglet.media.Player()
        
        #Event listener
        self.ui.addFile.clicked.connect(self.addFile)
        self.ui.play1.clicked.connect(self.playSong1)
        self.ui.stop1.clicked.connect(self.stopSong1)
        self.ui.backward1.clicked.connect(self.rewindSong1)
        self.ui.forward1.clicked.connect(self.nextSong1)
        self.ui.volume1.valueChanged.connect(self.setVolume1)
        self.ui.songLengthSlider1.sliderPressed.connect(self.songSlider1Pressed)
        self.ui.timestretch1.valueChanged.connect(self.setTimestretch1)
        
        self.ui.play2.clicked.connect(self.playSong2)
        self.ui.stop2.clicked.connect(self.stopSong2)
        self.ui.backward2.clicked.connect(self.rewindSong2)
        self.ui.forward2.clicked.connect(self.nextSong2)
        self.ui.volume2.valueChanged.connect(self.setVolume2)
        self.ui.songLengthSlider2.sliderPressed.connect(self.songSlider2Pressed)
        self.ui.timestretch2.valueChanged.connect(self.setTimestretch2) 

        #Run Pyglet 
        pyglet.app.run()

        #Execute User Interface
        sys.exit(self.app.exec_())

    # Return : Integer
    # Get selected index row from songlist 1
    def getSelectedIndex1(self):
        return [x.row() for x in self.ui.songList.selectedIndexes()][0]
    
    # Return : Integer
    # Get selected index row from songlist 2
    def getSelectedIndex2(self):
        return [x.row() for x in self.ui.songList2.selectedIndexes()][0]

    # Return : None
    # Set player 1 pitch everytime the timestretch dial value is changed, show a text
    # beside the dial representing the current BPM, and make the timer slower/faster based
    # on the pitch
    def setTimestretch1(self):
        try:
            self.player1.pitch = (self.ui.timestretch1.value() / 100000)
            self.ui.bpm1.setText(str(round(self.oriBpm1*self.player1.pitch,2)))
            if(self.playedAlready1 and not self.pauseState1):
                pyglet.clock.unschedule(self.timer1)
                pyglet.clock.schedule_interval(self.timer1, self.timeInterval/self.player1.pitch)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Choose A Song First')
            error_dialog.exec_()

    # Return : None
    # Set player 2 pitch everytime the timestretch dial value is changed, show a text
    # beside the dial representing the current BPM, and make the timer slower/faster based
    # on the pitch
    def setTimestretch2(self):
        try:
            self.player2.pitch = (self.ui.timestretch2.value() / 100000)
            self.ui.bpm2.setText(str(round(self.oriBpm2*self.player2.pitch,2)))
            if(self.playedAlready2 and not self.pauseState2):
                pyglet.clock.unschedule(self.timer2)
                pyglet.clock.schedule_interval(self.timer2, self.timeInterval/self.player2.pitch)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Choose A Song First')
            error_dialog.exec_()

    # Return : None
    # Pause the current song when the song length slider from player 1 is pressed, When
    # the slider is released go to setSongSlider1()
    def songSlider1Pressed(self):
        self.pauseSong1()
        self.ui.songLengthSlider1.sliderReleased.connect(self.setSongSlider1)

    # Return : None
    # Pause the current song when the song length slider from player 2 is pressed, When
    # the slider is released go to setSongSlider2()
    def songSlider2Pressed(self):
        self.pauseSong2()
        self.ui.songLengthSlider2.sliderReleased.connect(self.setSongSlider2)
    
    # Return : None
    # Take the value of song length slider from player 1 and change it to minute:second format,
    # change the value of the current timer, and play the song based on the new song slider position
    def setSongSlider1(self):
        min1,sec1 = divmod(self.ui.songLengthSlider1.value(), 60)
        self.time1 = self.ui.songLengthSlider1.value()
        min1 = round(min1)
        sec1 = round(sec1)
        currentTime1 = '{:02d}:{:02d}'.format(min1,sec1)
        self.ui.songLength1.setText(currentTime1)
        self.player1.seek(self.ui.songLengthSlider1.value())
        self.unpauseSong1()

    # Return : None
    # Take the value of song length slider from player 2 and change it to minute:second format,
    # change the value of the current timer, and play the song based on the new song slider position
    def setSongSlider2(self):
        min2,sec2 = divmod(self.ui.songLengthSlider2.value(), 60)
        self.time2 = self.ui.songLengthSlider2.value()
        min2 = round(min2)
        sec2 = round(sec2)
        currentTime2 = '{:02d}:{:02d}'.format(min2,sec2)
        self.ui.songLength2.setText(currentTime2)
        self.player2.seek(self.time2)
        self.unpauseSong2()

    # Return : None
    # Input the song file to song player 1 queue list to be played, get the BPM information,
    # get the song duration information, and set the song length slider range using the song
    # duration information 
    def songDetails1(self,index=None):
        if (index is None):
            self.playNow1 = self.playlist[self.getSelectedIndex1()][0]
        else:
            self.playNow1 = self.playlist[index][0]
            self.ui.songList.setCurrentRow(index)

        self.oriBpm1 = self.playlist[self.getSelectedIndex1()][1]
        
        if(self.bpm1Changed):
            self.bpmValue1 = (self.oriBpm2/self.oriBpm1)*100000
        
        self.source1 = pyglet.media.load(self.playNow1)
        self.player1.queue(self.source1)

        tempName1 = QUrl.fromLocalFile(self.playNow1)
        self.songName1,self.songFormat1= tempName1.fileName().rsplit('.',1)
        self.ui.songPlayed1.setText(self.songName1)
    
        self.songLength1 = self.source1.duration
        self.ui.songLengthSlider1.setRange(0,self.songLength1)

    # Return : None
    # Input the song file to song player 2 queue list to be played, get the BPM information,
    # get the song duration information, and set the song length slider range using the song
    # duration information 
    def songDetails2(self,index=None):
        if (index is None):
            self.playNow2 = self.playlist[self.getSelectedIndex2()][0]
        else:
            self.playNow2 = self.playlist[index][0]
            self.ui.songList2.setCurrentRow(index)
        
        self.oriBpm2 = self.playlist[self.getSelectedIndex2()][1]
        
        if(self.bpm2Changed):
            self.bpmValue2 = (self.oriBpm1/self.oriBpm2)*100000

        self.source2 = pyglet.media.load(self.playNow2)
        self.player2.queue(self.source2)

        tempName2 = QUrl.fromLocalFile(self.playNow2)
        self.songName2,self.songFormat2= tempName2.fileName().rsplit('.',1)
        self.ui.songPlayed2.setText(self.songName2)
            
        self.songLength2 = self.source2.duration
        self.ui.songLengthSlider2.setRange(0,self.songLength2)

    # Return : None
    # Add all of the mp3/wav files selected to the playlist, the information added on the 
    # playlists are filename, BPM, and time of the detected beat. Playlist format is an array with
    # 3 features ([filename][BPM][BeatTimes[]])
    def addToPlaylist(self,f):
        self.totalSong = len(f[0])
        for i in range(len(f[0])):
            tfm1 = sox.Transformer()
            sox_duration = sox.file_info.duration(f[0][i])
            tfm1.fade(fade_in_len=5)
            tfm1.trim(0, sox_duration-17)
            tfm1.build_file(f[0][i], 'C:\\Users\\Fadli\\Downloads\\Part1.wav')

            tfm2 = sox.Transformer()
            tfm2.trim(sox_duration-17, sox_duration-16.5)
            tfm2.bass(-5)
            tfm2.build_file(f[0][i], 'C:\\Users\\Fadli\\Downloads\\Part2.wav')

            tfm3 = sox.Transformer()
            tfm3.trim(sox_duration-16.5, sox_duration-16)
            tfm3.bass(-15)
            tfm3.build_file(f[0][i], 'C:\\Users\\Fadli\\Downloads\\Part3.wav')

            tfm4 = sox.Transformer()
            tfm4.trim(sox_duration-16, sox_duration)
            tfm4.fade(fade_out_len=16)
            tfm4.bass(-35)
            tfm4.build_file(f[0][i], 'C:\\Users\\Fadli\\Downloads\\Part4.wav')
            
            sox_output,_ = f[0][i].rsplit('.',1)
            sox_output += '.wav'

            cbn = sox.Combiner()
            cbn.build(['C:\\Users\\Fadli\\Downloads\\Part1.wav', 'C:\\Users\\Fadli\\Downloads\\Part2.wav', 'C:\\Users\\Fadli\\Downloads\\Part3.wav', 'C:\\Users\\Fadli\\Downloads\\Part4.wav'], sox_output , 'concatenate')
            
            tempSongname = QUrl.fromLocalFile(f[0][i])
            tempSongname,_ = tempSongname.fileName().rsplit('.',1)
            proc = madmom.features.beats.DBNBeatTrackingProcessor(fps=100)
            act = madmom.features.beats.RNNBeatProcessor(online=True,nn_files=[BEATS_LSTM[0]])(sox_output)
            beatTimes = proc(act)
            beatAvg = 0 
            for j in range(len(beatTimes)-1):
                beatAvg += 60/(beatTimes[j+1]-beatTimes[j])
            tempo = round(beatAvg/len(beatTimes))
            self.ui.songList.insertItem(self.index, tempSongname)
            self.ui.songList.setCurrentRow(0)
            self.ui.songList2.insertItem(self.index, tempSongname)
            self.ui.songList2.setCurrentRow(0)
            self.playlist[self.index].append(sox_output)
            self.playlist[self.index].append(tempo)
            self.playlist[self.index].append(beatTimes)
            self.playlist.append([])
            print(self.playlist)
            self.index +=1
            self.totalSong -=1

    # Return : None
    # Start a fade out effect on player 1 based on the length given by controlling the volume dial
    def fadeOut1(self,length):
        if(self.songLength1-self.time1 <= length):
            self.fadeValue1 -= ((self.timeInterval*1000)/length)
            self.ui.volume1.setValue(self.fadeValue1)
        
    # Return : None
    # Start a fade in effect on player 1 based on the length given by controlling the volume dial
    def fadeIn1(self,length):
        if(self.time1 <= length):
            self.fadeValue1 += ((self.timeInterval*1000)/length)
            self.ui.volume1.setValue(self.fadeValue1)
            
    # Return : None
    # Reset the bpm on the first player to its original value if the bpm is changed 
    def resetBpm1(self,start,duration):
        if(self.time1 >= start and self.ui.timestretch1.value() != 100000 and self.bpm1Changed):
            if(self.ui.timestretch1.value() > 100000):
                self.bpmValue1 -= (self.changedBpm1-100000)/(duration/self.timeInterval)
                self.ui.timestretch1.setValue(self.bpmValue1)
            else:
                self.bpmValue1 += (100000-self.changedBpm1)/(duration/self.timeInterval)
                self.ui.timestretch1.setValue(self.bpmValue1)
    
    # Return : None
    # Start a fade out effect on player 2 based on the length given by controlling the volume dial
    def fadeOut2(self,length):
        if(self.songLength2-self.time2 <= length):
            self.fadeValue2 -= ((self.timeInterval*1000)/length)
            self.ui.volume2.setValue(self.fadeValue2)

    # Return : None
    # Start a fade out effect on player 2 based on the length given by controlling the volume dial
    def fadeIn2(self,length):
        if(self.time2 <= length):
            self.fadeValue2 += ((self.timeInterval*1000)/length)
            self.ui.volume2.setValue(self.fadeValue2)  
    
    # Return : None
    # Reset the bpm on the second player to its original value if the bpm is changed 
    def resetBpm2(self,start,duration):
        if(self.time2 >= start and self.ui.timestretch2.value() != 100000 and self.bpm2Changed):
            if(self.ui.timestretch2.value() > 100000):
                self.bpmValue2 -= (self.changedBpm2-100000)/(duration/self.timeInterval)
                self.ui.timestretch2.setValue(self.bpmValue2)
            else:
                self.bpmValue2 += (100000-self.changedBpm2)/(duration/self.timeInterval)
                self.ui.timestretch2.setValue(self.bpmValue2)

    # Return : None
    # Start a timer for player 1 with +- 0,01 seconds precision, fade in for 10 secs when 
    # the song is played, fade out for 10 secs before the song ended, stop the song if it reaches
    # the maximum duration, and play the next song if the current duration equal to the last 10 beat time
    # value from song list 1 beat time array
    def timer1(self,dt):
        if(float(format(self.time1, '.2f')) == (float(format(self.playlist[self.getSelectedIndex1()][2][len(self.playlist[self.getSelectedIndex1()][2])-60],'.2f')))):    
            self.nextSong2(self.getSelectedIndex1()+1)
                
        if(self.time1 >= self.songLength1):
            self.stopSong1()

        self.time1 += dt
        self.curMin1,self.curSec1 = divmod(self.time1, 60)
        self.currentTime1 = '{:02d}:{:02d}'.format(int(self.curMin1),int(self.curSec1))
        self.ui.songLength1.setText(self.currentTime1)
        self.ui.songLengthSlider1.setValue(self.time1)
                   
        self.resetBpm1(25,10)
        self.fadeIn1(30)
        self.fadeOut1(30)

    # Return : None
    # Start a timer for player 2 with +- 0,01 seconds precision, fade in for 10 secs when 
    # the song is played, fade out for 10 secs before the song ended, stop the song if it reaches
    # the maximum duration, and play the next song if the current duration equal to the last 10 beat time
    # value from song list 2 beat time array
    def timer2(self,dt):
        if(self.time2 >= self.songLength2):
            self.stopSong2()

        if(float(format(self.time2, '.2f')) == (float(format(self.playlist[self.getSelectedIndex2()][2][len(self.playlist[self.getSelectedIndex2()][2])-60],'.2f')))):
            self.nextSong1(self.getSelectedIndex2()+1)

        # print(float(format(self.time2, '.2f')))
        # print((float(format(self.playlist[self.getSelectedIndex2()][2][len(self.playlist[self.getSelectedIndex2()][2])-40],'.2f'))))
        self.time2 += dt
        self.curMin2,self.curSec2 = divmod(self.time2, 60)
        self.currentTime2 = '{:02d}:{:02d}'.format(int(self.curMin2),int(self.curSec2))
        self.ui.songLength2.setText(self.currentTime2)
        self.ui.songLengthSlider2.setValue(self.time2)

        self.resetBpm2(25,10)
        self.fadeIn2(30)
        self.fadeOut2(30)
            
    # Return : None
    # Open an open file widget to add mp3/wav files to the songlist 1 and 2
    def addFile(self):
        filter = "MP3 (*.mp3);;WAV (*.wav)"
        self.file = QtWidgets.QFileDialog()
        self.file.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        self.filename = QtWidgets.QFileDialog.getOpenFileNames(filter=filter)
        self.addToPlaylist(self.filename)

    # Return : None
    # Play a queued song on player 1 and start the timer, if the song is currently playing the playedAlready1 flag will
    # change to True and plauseState1 flag will changed to False. If the pauseState1 equal to True it 
    # means the song is paused. If the song is played already, we can press the pause button to pause
    # and for unpausing we can use the same button.
    def playSong1(self):
        if(self.pauseState1):
            if(not self.playedAlready1):
                try:
                    self.fadeValue1 = 0
                    self.player1.delete()
                    self.player1 = pyglet.media.Player()
                    self.songDetails1()
                    if(self.aligned1):
                        self.player1.play()
                    else:
                        self.time1 = self.playlist[self.getSelectedIndex1()][2][0]
                        self.player1.seek(self.playlist[self.getSelectedIndex1()][2][0])
                        self.player1.play()
                    pyglet.clock.unschedule(self.timer1)
                    pyglet.clock.schedule_interval(self.timer1, self.timeInterval/self.player1.pitch) 
                    self.setTimestretch1()
                    self.setVolume1()
                    self.playedAlready1 = True
                    self.pauseState1 = False
                    self.ui.play1.setIcon(QtGui.QIcon("C:\\Users\\Fadli\\Desktop\\AI DJ\\Project AIDJ\\MusicPlayer\\pause.png"))
                except:
                    error_dialog = QtWidgets.QErrorMessage()
                    error_dialog.showMessage('Choose A Song First')
                    error_dialog.exec_()
            else:   
                self.unpauseSong1()
        else:
            self.pauseSong1()

    # Return : None
    # Play a queued song on player 2 and start the timer, if the song is currently playing the playedAlready2 flag will
    # change to True and plauseState1 flag will changed to False. If the pauseState2 equal to True it 
    # means the song is paused. If the song is played already, we can press the pause button to pause
    # and for unpausing we can use the same button.
    def playSong2(self):
        if(self.pauseState2):
            if(not self.playedAlready2):
                try:
                    self.fadeValue2 = 0
                    self.player2.delete()
                    self.player2 = pyglet.media.Player()
                    self.songDetails2()
                    if(self.aligned2):
                        self.player2.play()
                    else:
                        self.time2 = self.playlist[self.getSelectedIndex2()][2][0]
                        print(self.playlist[self.getSelectedIndex2()][2][0])
                        self.player2.seek(self.playlist[self.getSelectedIndex2()][2][0])
                        self.player2.play()
                    pyglet.clock.unschedule(self.timer2)
                    pyglet.clock.schedule_interval(self.timer2, self.timeInterval/self.player2.pitch) 
                    self.setTimestretch2()
                    self.setVolume2()
                    self.playedAlready2 = True
                    self.pauseState2 = False
                    self.ui.play2.setIcon(QtGui.QIcon("C:\\Users\\Fadli\\Desktop\\AI DJ\\Project AIDJ\\MusicPlayer\\pause.png"))
                except:
                    error_dialog = QtWidgets.QErrorMessage()
                    error_dialog.showMessage('Choose A Song First')
                    error_dialog.exec_()
            else:   
                self.unpauseSong2()
        else:
            self.pauseSong2()

    # Return : None
    # Pause the current song playing on player 1, pause the timer
    def pauseSong1(self):
        self.player1.pause()
        pyglet.clock.unschedule(self.timer1)
        self.ui.play1.setIcon(QtGui.QIcon("C:\\Users\\Fadli\\Desktop\\AI DJ\\Project AIDJ\\MusicPlayer\\play.png"))
        self.pauseState1 = True

    # Return : None
    # Pause the current song playing on player 2, pause the timer
    def pauseSong2(self):
        self.player2.pause()
        pyglet.clock.unschedule(self.timer2)
        self.ui.play2.setIcon(QtGui.QIcon("C:\\Users\\Fadli\\Desktop\\AI DJ\\Project AIDJ\\MusicPlayer\\play.png"))
        self.pauseState2 = True

    # Return : None
    # Unpause the current song playing on player 1, unpause the timer
    def unpauseSong1(self):
        self.player1.play()
        pyglet.clock.unschedule(self.timer1)
        pyglet.clock.schedule_interval(self.timer1, self.timeInterval/self.player1.pitch)
        self.pauseState1 = False
        self.ui.play1.setIcon(QtGui.QIcon("C:\\Users\\Fadli\\Desktop\\AI DJ\\Project AIDJ\\MusicPlayer\\pause.png"))

    # Return : None
    # Unpause the current song playing on player 2, unpause the timer
    def unpauseSong2(self):
        self.player2.play()
        pyglet.clock.unschedule(self.timer2)
        pyglet.clock.schedule_interval(self.timer2, self.timeInterval/self.player2.pitch)
        self.pauseState2 = False
        self.ui.play2.setIcon(QtGui.QIcon("C:\\Users\\Fadli\\Desktop\\AI DJ\\Project AIDJ\\MusicPlayer\\pause.png"))
 
    # Return : None
    # Stop the current song playing on player 1, reset the timer      
    def stopSong1(self):      
        self.player1.pause()
        self.player1.delete()
        self.playedAlready1 = False   
        self.pauseState1 = True
        self.length1 = '00:00'
        pyglet.clock.unschedule(self.timer1)
        self.time1 = 0
        self.ui.songLengthSlider1.setValue(0)
        self.ui.songLength1.setText(self.length1)  
        self.ui.play1.setIcon(QtGui.QIcon("C:\\Users\\Fadli\\Desktop\\AI DJ\\Project AIDJ\\MusicPlayer\\play.png")) 

    # Return : None
    # Stop the current song playing on player 2, reset the timer 
    def stopSong2(self):  
        self.player2.pause()
        self.player2.delete()
        self.playedAlready2 = False   
        self.pauseState2 = True
        self.length2 = '00:00'
        pyglet.clock.unschedule(self.timer2)
        self.time2 = 0
        self.ui.songLengthSlider2.setValue(0)
        self.ui.songLength2.setText(self.length2)  
        self.ui.play2.setIcon(QtGui.QIcon("C:\\Users\\Fadli\\Desktop\\AI DJ\\Project AIDJ\\MusicPlayer\\play.png"))\

    # Return : None
    # Set the volume of player 1
    def setVolume1(self):
        self.player1.volume = (self.ui.volume1.value() / 1000)

    # Return : None
    # Set the volume of player 2
    def setVolume2(self):
        self.player2.volume = (self.ui.volume2.value() / 1000)

    # Return : None
    # Rewind the song of player 1, if its less than 5 seconds go back to the previous song
    def rewindSong1(self):
        if(self.time1 < 5 and (self.getSelectedIndex1()) != 0):
            self.songDetails1(self.getSelectedIndex1()-1)
            self.stopSong1()
            self.playSong1()
        else:
            self.stopSong1()
            self.playSong1()

    # Return : None
    # Rewind the song of player 2, if its less than 5 seconds go back to the previous song
    def rewindSong2(self):
        if(self.time2 < 5 and (self.getSelectedIndex2()) != 0):
            self.songDetails2(self.getSelectedIndex2()-1)
            self.stopSong2()
            self.playSong2()
        else:
            self.stopSong2()
            self.playSong2()

    # Return : None
    # Change the bpm of the first player to match the bpm of the previous song
    def changeBpm1(self):
        self.ui.timestretch1.setValue((self.oriBpm2/self.oriBpm1)*100000)
        self.changedBpm1 = self.ui.timestretch1.value()
        self.bpm1Changed = True
        self.aligned1 = False

    # Return : None
    # Change the bpm of the second player to match the bpm of the previous song
    def changeBpm2(self):
        self.ui.timestretch2.setValue((self.oriBpm1/self.oriBpm2)*100000)
        self.changedBpm2 = self.ui.timestretch2.value()
        self.bpm2Changed = True  
        self.aligned2 = False

    # Return : None
    # Play the next song of player 1, if index is specified jump to the song that has the same song index
    def nextSong1(self,songIndex=None):
        if(songIndex is not False and ((self.getSelectedIndex2()) != self.index-1)):
            self.songDetails1(songIndex)
            self.changeBpm1()
            self.stopSong1()
            self.playSong1()
        elif(songIndex is False and ((self.getSelectedIndex1()) != self.index-1)):
            self.songDetails1(self.getSelectedIndex1()+1)
            self.stopSong1()
            self.playSong1()
        else:
            self.changeBpm1()
            self.stopSong1()
            self.playSong1()  

    # Return : None
    # Play the next song of player 2, if index is specified jump to the song that has the same song index
    def nextSong2(self,songIndex=None):
        if(songIndex is not False and ((self.getSelectedIndex1()) != self.index-1)):
            self.songDetails2(songIndex)
            self.changeBpm2()
            self.stopSong2()
            self.playSong2()
        elif(songIndex is False and ((self.getSelectedIndex2()) != self.index-1)):
            self.songDetails2(self.getSelectedIndex2()+1)
            self.stopSong2()
            self.playSong2()
        else:
            self.changeBpm2()
            self.stopSong2()
            self.playSong2()   

    # def aidjMode(self):
    #     self.playSong1()
 
if __name__ == "__main__":
        play = MusicPlayer()
        
        
        