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
import os

import cv2
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot

import common.modulemanager
# import delayvideo.video.video
import delayvideo.video.framebuffer
import settings.settingsmanager
import ui.mainwindow
import ui.overlay

# try:
#     import psutil
# except:
#     psutil = None


class DelayVideoApplication(QtCore.QObject):
    '''Performs the main logic/connections in the application'''
    
    def __init__(self, argv = [], parent=None):
        '''Performs the main logic/connections in the application'''
        
        QtCore.QObject.__init__(self, parent)
        
        #TODO: write startup file and log
        
        # load settings file
        if len(argv) == 2:
            self.settings = settings.settingsmanager.SettingsManager(argv[1])
        else:
            self.settings = settings.settingsmanager.SettingsManager()
        
        # setup main window
        self.mainwindow = ui.mainwindow.MainWindow(self.settings, self)
        self.mainwindow.show()
        
        # add overlay
        self.overlay = ui.overlay.OverlayWidget(self.mainwindow)
        self.overlay.addMessage("Loading ...", timeout=self.settings.getSetting('delay'))
        
        # connect signals
        self.mainwindow.incDelay.connect(self.incDelay)
        self.mainwindow.decDelay.connect(self.decDelay)
        self.mainwindow.incFrame.connect(self.incFrame)
        self.mainwindow.decFrame.connect(self.decFrame)
        self.mainwindow.togglePlay.connect(self.togglePlay)
        self.mainwindow.recordBuffer.connect(self.recordBuffer)
        
        # get layout
        sellayout = self.settings.getSetting('selectedlayout')
        try:
            layout = self.settings.getSetting('layouts')[sellayout]
        except:
            layout = self.settings.getSetting('layouts')[0]
        self.overlay.addMessage("Layout: %s"%layout['name'])
        
        # construct capture objects
        self._captureframes = []
        for cap in layout['captureframe']:
            self._captureframes.append(common.modulemanager.ModuleManager.getCaptureFrameModule(cap[0]).getModule(cap[1]))
        
        # frame buffer
#         self.video = delayvideo.video.video.Video(cv2.VideoCapture(0))
        self.framebuffer = delayvideo.video.framebuffer.FrameBuffer(self.settings)    # place to store frames while running
        self.pausedbuffer = None            # place to store frames while paused
        
        # frame capture timer
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.frame)
        self._timer.start(27)
        
        # save settings timer
        self._savetimer = QtCore.QTimer(self)
        self._savetimer.timeout.connect(self.settings.writeSettings)
        self._savetimer.start(5000) # 5sec (only if needed)
        
        # statevars
        self.framei = 0
        self.paused = False
    
    def cleanup(self):
        '''Called just before closing application'''
        # save the settings (only if changed)
        if self.settings:
            self.settings.writeSettings()
        #TODO: remove startup file (to check for crashes)
    
    def frame(self):
        '''Called to capture next frame (and cause a previous one to display)'''
        
        try:
            # capture and store frame frame
            frameset = []
            for cap in self._captureframes:
                frameset.append(cap.getFrame())
            
            # process frameset
            self.framebuffer.push(frameset[0].asQPixmap())
            
            # display next frame
            delayedframe = self.framebuffer.get()
            if not self.paused:
                self.mainwindow.updateView(0,delayedframe)
            
            # display stats and buffering message (if required)
            self.framei = (self.framei + 1) % 10
            if self.framei == 0:
                self.mainwindow.setFrameRate("%.2f"%self.framebuffer.getFrameRate())
        except TypeError:
            pass
    
    
    @pyqtSlot()
    def incDelay(self):
        '''
        Increases delay by 0.5 seconds
        @return: float, the new delay
        '''
        delay = float(self.settings.getSetting("delay")) + 0.5
        if delay < 0:
            delay = 0
        self.settings.setSetting("delay", delay)
        self.overlay.addMessage("Delay: %ss"%delay)
        return delay
    
    @pyqtSlot()
    def decDelay(self):
        '''
        Decreases delay by 0.5 seconds
        
        @return: float, the new delay
        '''
        delay = float(self.settings.getSetting("delay")) - 0.5
        if delay < 0:
            delay = 0.0
        self.settings.setSetting("delay", delay)
        self.overlay.addMessage("Delay: %ss"%delay)
        return delay
    
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
        self.pausedbuffer = None
        self.updateFrameId()
    
    @pyqtSlot()
    def recordBuffer(self):
        if self.pausedbuffer:
            self.pausedbuffer.writeToDir("%s%svideo_%s" % (self.settings.getSetting("recorddirectory"), os.path.sep, time.strftime("%Y-%m-%d_%H-%M-%S"), ))

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
    