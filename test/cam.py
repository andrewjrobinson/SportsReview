#!/bin/env python
'''
test.cam -- shortdesc

test.cam is a description

It defines classes_and_methods

@author:     Andrew Robinson
        
@copyright:  2014 Andrew Robinson. All rights reserved.
        
@license:    LGPL3+

@contact:    andrewjrobinson@gmail.com
'''
import sys

import cv2
from PyQt4 import QtGui, QtCore, Qt
from ui import Ui_MainWindow
from video import Video
 
class Gui(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.video = Video(cv2.VideoCapture(0))
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()
 
    def play(self):
        try:
            self.video.captureFrame()
            self.ui.videoFrame.setPixmap(
                self.video.convertFrame())
            self.ui.videoFrame.setScaledContents(True)
        except TypeError:
            print "No frame"
 
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    ex.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
