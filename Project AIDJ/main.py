import sys
import platform
import madmom 
import librosa, librosa.display, matplotlib.pyplot as plt
import IPython.display as ipd 
from madmom.models import BEATS_LSTM
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from maingui import Ui_SplashScreen

class ui_bpm:
        def __init__(self):
                app = QtWidgets.QApplication(sys.argv)
                self.SplashScreen = QtWidgets.QMainWindow()
                self.ui = Ui_SplashScreen()
                self.ui.setupUi(self.SplashScreen)
                self.SplashScreen.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
                self.SplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent
                self.SplashScreen.show()
                self.ui.pushButton.clicked.connect(self.checkBpm)
                sys.exit(app.exec_())
        
        def checkBpm(self):
                filename = QFileDialog.getOpenFileName()
                x,sr=librosa.core.load(filename[0])
                proc = madmom.features.beats.DBNBeatTrackingProcessor(fps=200)
                act = madmom.features.beats.RNNBeatProcessor(online=True,nn_files=[BEATS_LSTM[0]])(filename[0])
                #average bpm detection
                beat_times = proc(act)
                beat_avg = 0 
                for i in range(len(beat_times)-1):
                        beat_avg += 60/(beat_times[i+1]-beat_times[i])
                bpmFloat = str(round(beat_avg/len(beat_times)))
                bpm, throw = bpmFloat.split('.')
                self.ui.label_2.setText(bpm)

if __name__ == "__main__":
        test = ui_bpm()
        