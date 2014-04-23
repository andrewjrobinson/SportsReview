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
        
        # load settings file
        if len(argv) == 2:
            self.settings = sportsreview.settings.settingsmanager.SettingsManager(argv[1])
        else:
            self.settings = sportsreview.settings.settingsmanager.SettingsManager()
        
        # setup main window
        self.mainwindow = mainwindow.MainWindow(self.settings, self)
        
        # connect signals
        self.mainwindow.openFile.connect(self.openFile)
        
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
        self.mainwindow.setStatusMsg("Opened: %s" % (filename, ))
        
    @Slot()
    def nextFrame(self):
        '''Change to the next frame'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.next()
            self.selectedFrameSet.emit(self._openFrameGroup, self._openFrameGroup.index())
    
    @Slot()
    def prevFrame(self):
        '''Change to the previous frame'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.prev()
            self.selectedFrameSet.emit(self._openFrameGroup, self._openFrameGroup.index())
    
    @Slot(int)
    def setFrame(self, idx):
        '''Change to a specified frame'''
        if self._openFrameGroup is not None:
            self._openFrameGroup.setPosition(idx)
            self.selectedFrameSet.emit(self._openFrameGroup, self._openFrameGroup.index())
            
    @Slot(float)
    def play(self, speed):
        '''Play current file at selected speed.  Can call it multiple times to change speed.'''
        if not self._playingTimer.isActive():
            self._playing = speed
            now = time.time()
            self._playStartOffset = now - self._openFrameGroup.current().timestamp
            self._playingTimer.start(16) #Todo: make this a setting (16 = 62.5 fps (max))
        else:
            pass #TODO: alter start time so it will calculate correctly
        
    ## Support ##
    def _playFrame(self):
        '''Plays the next frame if required [timer target]'''
        
        # stop timer if we are paused (i.e. speed 0)
        if self._playing == 0:
            self._playingTimer.stop()
            return
        
        # find the last release-able frame
        now = time.time()
        nextFrame = self._openFrameGroup.peekNext()
        lastFrame = None
        while nextFrame is not None and \
                (nextFrame.timestamp + self._playStartOffset) < now:
            lastFrame = self._openFrameGroup.next()
            nextFrame = self._openFrameGroup.peekNext()
        
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
