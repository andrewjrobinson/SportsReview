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
#  *  along with SportsReview.  If not, see <http://www.gnu.org/licenses/>.      *
#  *                                                                             *
#  *******************************************************************************/
import traceback
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
import common.frameset
import common.framegroup
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
        self.mainwindow.processFrame.connect(self.processFrame)
        self.mainwindow.processGroup.connect(self.processGroup)
        
        # get layout
        sellayout = self.settings.getSetting('selectedlayout')
        try:
            layout = self.settings.getSetting('layouts')[sellayout]
        except:
            layout = self.settings.getSetting('layouts')[0]
        self.overlay.addMessage("Layout: %s"%layout['name'], group='layout')
        
        # construct capture objects
        self._captureframes = []
        for cap in layout['captureframe']:
            self._captureframes.append(common.modulemanager.ModuleManager.getCaptureFrameModule(cap[0]).getModule(self.settings, cap[1]))
        
        # frame processors (delay and buffering)
        self._processframes = []
        for cap in layout['processframe']:
            self._processframes.append(common.modulemanager.ModuleManager.getProcessFrameModule(cap[0]).getModule(self.settings, cap[1]))
        self.pausedbuffer = None            # place to store frames while paused
        
        self._processgrouprandom = {}
        
        # frame capture timer
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.frame)
        self._timer.start(27) #Todo: make this a setting
        
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
          
        # capture and store frame from each capture device
        frameset = common.frameset.FrameSet(time.time())
        for cap in self._captureframes:
            frameset.addFrame(cap.getFrame())
        
        # process the frameset through the pipeline
        procframeset = frameset
        for proc in self._processframes:
            procframeset = proc.process(procframeset)
        
        # display processed (probably delayed) frame
        if not self.paused and procframeset is not None:
            self.mainwindow.renderFrameset(procframeset)
        
        # display stats and buffering message (if required)
#         self.framei = (self.framei + 1) % 10
#         if self.framei == 0:
#             self.mainwindow.setFrameRate("%.2f"%self.framebuffer.getFrameRate())
    
    
    @pyqtSlot()
    def incDelay(self):
        '''
        Increases delay by 0.5 seconds
        @return: float, the new delay
        '''
        if not self.paused:
            delay = float(self.settings.getSetting("delay")) + 0.5
            if delay > 20:
                delay = 20.0
            self.settings.setSetting("delay", delay)
            self.overlay.addMessage("Delay: %ss"%delay)
    
    @pyqtSlot()
    def decDelay(self):
        '''
        Decreases delay by 0.5 seconds
        
        @return: float, the new delay
        '''
        if not self.paused:
            delay = float(self.settings.getSetting("delay")) - 0.5
            if delay < 0:
                delay = 0.0
            self.settings.setSetting("delay", delay)
            self.overlay.addMessage("Delay: %ss"%delay)
    
    @pyqtSlot()
    def incFrame(self):
        if self.paused and self.pausedbuffer:
            frameset = self.pausedbuffer.next()
            if frameset is not None:
                self.mainwindow.renderFrameset(frameset)
                self.updateFrameId()
    
    @pyqtSlot()
    def decFrame(self):
        if self.paused and self.pausedbuffer:
            frameset = self.pausedbuffer.prev()
            if frameset is not None:
                self.mainwindow.renderFrameset(frameset)
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
        
        # copy frames
        self.pausedbuffer = common.framegroup.FrameGroup()
        for proc in self._processframes:
            proc.giveFrames(self.pausedbuffer)
            
        # update UI
        self.mainwindow.renderFrameset(self.pausedbuffer.current())
        self.updateFrameId()
    
    @pyqtSlot()
    def play(self):
        self.paused = False
        self.pausedbuffer = None
        self.updateFrameId()
    
    @pyqtSlot(str, object)
    def processFrame(self, modulename, config):
        ''''''
        if self.paused:
            # get module implementation
            if modulename in self._processframerandom:
                module = self._processframerandom[modulename]
            else:
                module = common.modulemanager.ModuleManager.getProcessFrameModule(modulename).getModule(self.settings, config)
                self._processframerandom[modulename] = module
            
            module.process(self.pausedbuffer.current())
        
    @pyqtSlot(str, object)
    def processGroup(self, modulename, config):
        ''''''
        if self.paused:
            # get module implementation
            if modulename in self._processgrouprandom:
                module = self._processgrouprandom[modulename]
            else:
                module = common.modulemanager.ModuleManager.getProcessGroupModule(modulename).getModule(self.settings, config)
                self._processgrouprandom[modulename] = module
                
            module.processGroup(self.pausedbuffer)
    
    def updateFrameId(self):
        if self.pausedbuffer and self.paused:
            self.mainwindow.setFrameId("%s/%s" % (self.pausedbuffer.index() + 1, len(self.pausedbuffer)))
        else:
            self.mainwindow.setFrameId("~")


def main(argv):
    
    args = argv[1:]
    args.insert(0, "Delay Analysis")
    app = QtGui.QApplication(args)
    runtime = DelayVideoApplication()
    rc = app.exec_()
    runtime.cleanup()
    sys.exit(rc)
 
if __name__ == '__main__':
    main(sys.argv)
    