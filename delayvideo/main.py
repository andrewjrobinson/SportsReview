# /*******************************************************************************
#  *   (c) Andrew Robinson (andrewjrobinson@gmail.com) 2014                      *
#  *                                                                             *
#  *  This file is part of SportsReview.                                         *
#  *                                                                             *
#  *  SportsReview is free software: you can redistribute it and/or modify       *
#  *  it under the terms of the GNU Lesser General Public License as published   *
#  *  by the Free Software Foundation, either version 3 of the License, or       *
#  *  (at your option) any later version.                                        *
#  *                                                                             *
#  *  SportsReview is distributed in the hope that it will be useful,            *
#  *  but WITHOUT ANY WARRANTY; without even the implied warranty of             *
#  *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              *
#  *  GNU Lesser General Public License for more details.                        *
#  *                                                                             *
#  *  You should have received a copy of the GNU Lesser General Public License   *
#  *  along with QualityTrim.  If not, see <http://www.gnu.org/licenses/>.       *
#  *                                                                             *
#  *******************************************************************************/
'''
Created on 22/03/2014

@author: arobinson
'''

import sys
import time

import cv2
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import pyqtSlot

# from ui.ui import Ui_MainWindow
import ui.mainwindow
import settings.settingsmanager
import delayvideo.video.video
import delayvideo.video.framebuffer
# from video import Video
# from framebuffer import FrameBuffer

# try:
#     import psutil
# except:
#     psutil = None


class DelayVideoApplication(QtCore.QObject):
    '''Performs the main logic/connections in the application'''
    
    def __init__(self, argv = [], parent=None):
        QtCore.QObject.__init__(self, parent)
        
        #TODO: write startup file
        
        # load settings file
        if len(argv) == 2:
            self.settings = settings.settingsmanager.SettingsManager(argv[1])
        else:
            self.settings = settings.settingsmanager.SettingsManager()
        
        # setup main window
        self.mainwindow = ui.mainwindow.MainWindow(self)
        self.mainwindow.show()
        
        # connect signals
        self.mainwindow.incDelay.connect(self.incDelay)
        self.mainwindow.decDelay.connect(self.decDelay)
        self.mainwindow.incFrame.connect(self.incFrame)
        self.mainwindow.decFrame.connect(self.decFrame)
        self.mainwindow.togglePlay.connect(self.togglePlay)
        self.mainwindow.recordBuffer.connect(self.recordBuffer)
        
        # get capturer and frame buffer
        self.video = delayvideo.video.video.Video(cv2.VideoCapture(0))
        self.framebuffer = delayvideo.video.framebuffer.FrameBuffer()    # place to store frames while running
        self.pausedbuffer = None            # place to store frames while paused
        
        # frame capture timer
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.frame)
        self._timer.start(27)
        
        # statevars
        self.framei = 0
        self.paused = False
    
    def cleanup(self):
        ''''''
        #TODO: remove startup file (to check for crashes)
    
    def frame(self):
        '''Called to capture next frame (and cause a previous one to display)'''
        
        try:
            # capture and store frame frame
            self.video.captureFrame()
            self.framebuffer.push(self.video.convertFrame())
            
            # display next frame
            delayedframe = self.framebuffer.get()
            if not self.paused:
                self.mainwindow.updateView(0,delayedframe)
            
            # display stats and buffering message (if required)
            self.framei = (self.framei + 1) % 10
            if self.framei == 0:
                self.mainwindow.setFrameRate("%.2f"%self.framebuffer.getFrameRate())
            if delayedframe:
                self.mainwindow.updateViewText("")
            else:
                self.mainwindow.updateViewText("Buffering ...")
        except TypeError:
            self.mainwindow.updateViewText("Buffering ...")
    
    @pyqtSlot()
    def incDelay(self):
        self.framebuffer.incDelay()
        self.mainwindow.setDelay("%.1f"%self.framebuffer._delay)
    
    @pyqtSlot()
    def decDelay(self):
        self.framebuffer.decDelay()
        self.mainwindow.setDelay("%.1f"%self.framebuffer._delay)
    
    @pyqtSlot()
    def incFrame(self):
        if self.paused and self.pausedbuffer:
            frame = self.pausedbuffer.next()
            if frame:
                self.mainwindow.updateView(0, frame)
                self.updateFrameId()
    
    @pyqtSlot()
    def decFrame(self):
        if self.paused and self.pausedbuffer:
            frame = self.pausedbuffer.prev()
            if frame:
                self.mainwindow.updateView(0, frame)
                self.updateFrameId()
    
    @pyqtSlot()
    def togglePlay(self):
        if self.paused:
            self.play()
        else:
            self.pause()
    
    @pyqtSlot()
    def pause(self):
        self.paused = True
        self.pausedbuffer = self.framebuffer.cloneFrames()
        self.mainwindow.updateView(0, self.pausedbuffer.current())
        self.updateFrameId()
    
    @pyqtSlot()
    def play(self):
        self.paused = False
        self.pausedbuffer = None  #NOTE: maybe we shouldn't clear it hear so they can record if after resuming.
        self.updateFrameId()
    
    @pyqtSlot()
    def recordBuffer(self):
        if self.pausedbuffer:
            self.pausedbuffer.writeToDir("/tmp/video_%s" % time.strftime("%Y-%m-%d_%H-%M-%S"))

    def updateFrameId(self):
        if self.pausedbuffer and self.paused:
            self.mainwindow.setFrameId("%s/%s" % (self.pausedbuffer._frameidx + 1, len(self.pausedbuffer._frames)))
        else:
            self.mainwindow.setFrameId("~")


def main(argv):
    
    app = QtGui.QApplication(argv)
    runtime = DelayVideoApplication()
    rc = app.exec_()
    runtime.cleanup()
    sys.exit(rc)
 
if __name__ == '__main__':
    main(sys.argv)
    