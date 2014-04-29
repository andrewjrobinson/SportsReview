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
import time
'''
Created on 18/04/2014
@author: Andrew Robinson
'''
import sys

from sportsreview.support.qtlib import QtCore, QtGui, Slot, Signal

import sportsreview.common.modulemanager
import sportsreview.settings.settingsmanager

import mainwindow


class AfterTouchesApplication(QtCore.QObject):
    '''Performs the main logic/connections in the application'''
    
    def __init__(self, argv = [], parent=None):
        '''Performs the main logic/connections in the application'''
        
        QtCore.QObject.__init__(self, parent)
        
        self._openFrameGroup = None
        
        self._processframerandom = {}
        self._processgrouprandom = {}
        
        # load settings file
        if len(argv) == 2:
            self.settings = sportsreview.settings.settingsmanager.SettingsManager(argv[1])
        else:
            self.settings = sportsreview.settings.settingsmanager.SettingsManager()
        
        # setup main window
        self.mainwindow = mainwindow.MainWindow(self.settings, self)
        
        # connect signals
        self.mainwindow.openFile.connect(self.openFile)
        self.mainwindow.processFrame.connect(self.processFrame)
        self.mainwindow.processGroup.connect(self.processGroup)
        
        # frame playback timer
        self._playing = 0 #speed, 1 = normal, 0.5 = half speed (in future: -ve for reverse)
        self._playStartOffset = 0 #the difference between system time and frameset timestamps
        self._playingTimer = QtCore.QTimer(self)
        self._playingTimer.timeout.connect(self._playFrame)
        
        # show main window
        self.mainwindow.show()
    
    def cleanup(self):
        '''Called just before closing application'''
        # save the settings (only if changed)
        if self.settings:
            self.settings.writeSettings()
    
    ## signals ##
    openFrameGroup = Signal(object)         # emitted when the frameGroup is changed
    selectedFrameSet = Signal(object, int)  # emitted when a new frameset is selected
    
    ## slots ##
    @Slot(str)
    def openFile(self, filename):
        '''Open the given file'''
        self.mainwindow.setStatusMsg("Opening: %s" % (filename, ))
        reader = sportsreview.common.modulemanager.ModuleManager.getCaptureGroupModule("JpegStillArrayReader").getModule(self.settings, {})
        fgroup = reader.load({"filename": filename})
        self._openFrameGroup = fgroup
        self.openFrameGroup.emit(fgroup)
        self.mainwindow.setStatusMsg("Opened: %s" % (filename, ), 5000)
        
    @Slot()
    def nextFrame(self):
        '''Change to the next frame'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.next()
            self.selectedFrameSet.emit(self._openFrameGroup, self._openFrameGroup.index())
        else:
            self.mainwindow.setStatusMsg("No file open!", 1000)
    
    @Slot()
    def prevFrame(self):
        '''Change to the previous frame'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.prev()
            self.selectedFrameSet.emit(self._openFrameGroup, self._openFrameGroup.index())
        else:
            self.mainwindow.setStatusMsg("No file open!", 1000)
    
    @Slot(int)
    def setFrame(self, idx):
        '''Change to a specified frame'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.setPosition(idx)
            self.selectedFrameSet.emit(self._openFrameGroup, self._openFrameGroup.index())
        else:
            self.mainwindow.setStatusMsg("No file open!", 1000)
            
    @Slot()
    def jumpStart(self):
        '''Move the start of current framegroup'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.setPosition(self._openFrameGroup.getClipStart())
            self.selectedFrameSet.emit(self._openFrameGroup, self._openFrameGroup.index())
        else:
            self.mainwindow.setStatusMsg("No file open!", 1000)
        
    @Slot()
    def jumpEnd(self):
        '''Move to the end of current framegroup'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.setPosition(self._openFrameGroup.getClipEnd() - 1)
            self.selectedFrameSet.emit(self._openFrameGroup, self._openFrameGroup.index())
        else:
            self.mainwindow.setStatusMsg("No file open!", 1000)
        
    @Slot(float)
    def play(self, speed):
        '''Play current file at selected speed.  Can call it multiple times to change speed.'''
        if self._openFrameGroup is not None:
            if speed == 0:
                self.mainwindow.setStatusMsg("Paused", 1000)
            elif speed > 0: # forward
                if self._openFrameGroup.index() >= (self._openFrameGroup.getClipEnd() - 1):
                    self.jumpStart()
                self.mainwindow.setStatusMsg("Play (%sx)" % speed, 1000)
                startTime = time.time() + (self._openFrameGroup[self._openFrameGroup.getClipStart()].timestamp - self._openFrameGroup.current().timestamp) / speed
            else:           # reverse
                if self._openFrameGroup.index() <= self._openFrameGroup.getClipStart():
                    self.jumpEnd()
                self.mainwindow.setStatusMsg("Play reverse (%sx)" % (-speed), 1000)
                startTime = time.time() - (self._openFrameGroup.current().timestamp - self._openFrameGroup[self._openFrameGroup.getClipEnd()-1].timestamp) / speed
            if not self._playingTimer.isActive():
                self._playing = speed
                self._playStartTime = startTime
                self._playingTimer.start(16) #Todo: make this a setting (16 = 62.5 fps (max))
            else:
                pass #TODO: alter start time so it will calculate correctly
        else:
            self.mainwindow.setStatusMsg("No file open!", 1000)
    
    @Slot(str, object)
    def processFrame(self, modulename, config):
        ''''''
        if self._openFrameGroup is not None:
            # get module implementation
            if modulename in self._processframerandom:
                module = self._processframerandom[modulename]
            else:
                module = sportsreview.common.modulemanager.ModuleManager.getProcessFrameModule(modulename).getModule(self.settings, config)
                self._processframerandom[modulename] = module
            
            module.process(self._openFrameGroup.current())
        
    @Slot(str, object)
    def processGroup(self, modulename, config):
        ''''''
        if self._openFrameGroup is not None:
            # get module implementation
            if modulename in self._processgrouprandom:
                module = self._processgrouprandom[modulename]
            else:
                module = sportsreview.common.modulemanager.ModuleManager.getProcessGroupModule(modulename).getModule(self.settings, config)
                self._processgrouprandom[modulename] = module
                
            module.processGroup(self._openFrameGroup)
        
    @Slot()
    def clipStart(self):
        '''Mark current frame as start'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.clipStart()
        else:
            self.mainwindow.setStatusMsg("No file open!", 1000)
        
    @Slot()
    def clipEnd(self):
        '''Mark current frame as end'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.clipEnd()
        else:
            self.mainwindow.setStatusMsg("No file open!", 1000)
    
    ## Support ##
    def _playFrame(self):
        '''Plays the next frame if required [timer target]'''
        
        # stop timer if we are paused (i.e. speed 0)
        if self._playing == 0:
            self._playingTimer.stop()
            return
        
        # find the last release-able frameset
        playbackTime = (time.time() - self._playStartTime) * self._playing
        lastFrame = None
        nextFrame = None
        if self._playing > 0:   # playing forward
            releaseTimestamp = float(self._openFrameGroup[self._openFrameGroup.getClipStart()].timestamp) + playbackTime
            nextFrame = self._openFrameGroup.peekNext()
            if self._openFrameGroup.index() >= self._openFrameGroup.getClipEnd():
                nextFrame = None
            while nextFrame is not None and nextFrame.timestamp < releaseTimestamp:
                lastFrame = self._openFrameGroup.next()
                nextFrame = self._openFrameGroup.peekNext()
                if self._openFrameGroup.index() >= (self._openFrameGroup.getClipEnd() - 1):
                    nextFrame = None
        else:                   # playing reverse
            releaseTimestamp = float(self._openFrameGroup[self._openFrameGroup.getClipEnd()-1].timestamp) + playbackTime
            nextFrame = self._openFrameGroup.peekPrev()
            if self._openFrameGroup.index() <= self._openFrameGroup.getClipStart():
                nextFrame = None
            while nextFrame is not None and nextFrame.timestamp > releaseTimestamp:
                lastFrame = self._openFrameGroup.prev()
                nextFrame = self._openFrameGroup.peekPrev()
                if self._openFrameGroup.index() < self._openFrameGroup.getClipStart():
                    nextFrame = None
                
        # display the last released frame (if required)
        if lastFrame is not None:
            self.selectedFrameSet.emit(self._openFrameGroup, self._openFrameGroup.index())
            
        # stop timer at end
        if nextFrame is None:
            self._playingTimer.stop()
            self._playing = 0
    
# end class

def main(argv):
    
    args = argv[1:]
    args.insert(0, "After Touches")
    app = QtGui.QApplication(args)
    runtime = AfterTouchesApplication()
    rc = app.exec_()
    runtime.cleanup()
    sys.exit(rc)
 
if __name__ == '__main__':
    main(sys.argv)
