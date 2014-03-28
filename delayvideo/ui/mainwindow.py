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
Creates and manages the main window from the ui.py file

Created on 26/03/2014

@author: arobinson
'''

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from ui import Ui_MainWindow
import time


class MainWindow(QtGui.QMainWindow):
    def __init__(self,application=None):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update()
        self.application = application
    
    # signals
    incDelay = pyqtSignal()         #+>=. (while running)
    decDelay = pyqtSignal()         #-<,  (while running)
    incFrame = pyqtSignal()         #+>=. (while paused)
    decFrame = pyqtSignal()         #-<,  (while paused)
    help = pyqtSignal()             #F1
    edit = pyqtSignal()             #F2
    togglePlay = pyqtSignal()       #F7 <space>
    recordBuffer = pyqtSignal()     #F12
    
    
    def interuptClose(self):
        '''Call this in closing signal to abort close'''
        self.abortClose = True
    
    def _doClose(self):
        '''signal and then close (if required)'''
        self.abortClose = False
        self.closing.emit()
        if not self.abortClose:
            self.cl
        
    
    def keyPressEvent(self, e):
        '''Perform tasks for various key events'''
        
        # quit
        if e.key() in (QtCore.Qt.Key_Escape, QtCore.Qt.Key_Q):
            self.close()
            
        # increase (delay or frame)
        elif e.key() in (QtCore.Qt.Key_Greater, QtCore.Qt.Key_Plus, QtCore.Qt.Key_Equal, QtCore.Qt.Key_Period):
            if self.application.paused:
                self.incFrame.emit()
            else:
                self.incDelay.emit()
        
        # decrease (delay or frame)
        elif e.key() in (QtCore.Qt.Key_Less, QtCore.Qt.Key_Minus, QtCore.Qt.Key_Comma):
            if self.application.paused:
                self.decFrame.emit()
            else:
                self.decDelay.emit()
                
        elif e.key() == QtCore.Qt.Key_F1:
            self.help.emit()
                
        elif e.key() == QtCore.Qt.Key_F2:
            self.edit.emit()
                
        elif e.key() in (QtCore.Qt.Key_F7, QtCore.Qt.Key_Space):
            self.togglePlay.emit()
                
        elif e.key() == QtCore.Qt.Key_F11:
            if not self.isFullScreen():
                self.showFullScreen()
            else:
                self.showNormal()
                
        elif e.key() == QtCore.Qt.Key_F12:
            self.recordBuffer.emit()
        else:
            print "key: %s" % (e.key(),)
    
    def updateView(self, vid, pixmap):
        '''Updates a view to display given pixmap'''
        self.ui.videoFrame.setPixmap(pixmap)
        self.ui.videoFrame.setScaledContents(True)
        
    def updateViewText(self, text):
        self.ui.videoFrame.setText(text)
    
    def setFrameId(self, frameid):
        self.ui.frameNum.setText(frameid)
        
    def setFrameRate(self, framerate):
        self.ui.frameRate.setText(framerate)
        
    def setDelay(self, delay):
        self.ui.delay.setText(delay)
        
#     @pyqtSlot()
#     def incDelay(self):
#         self.framebuffer.incDelay()
#         self.ui.delay.setText("%.1f"%self.framebuffer._delay)
#     
#     @pyqtSlot()
#     def decDelay(self):
#         self.framebuffer.decDelay()
#         self.ui.delay.setText("%.1f"%self.framebuffer._delay)
#     
#     @pyqtSlot()
#     def pauseClicked(self):
#         self.paused = True
#         self.pausedbuffer = self.framebuffer.cloneFrames()
#         self.ui.videoFrame.setPixmap(self.pausedbuffer.current())
#         self.ui.videoFrame.setScaledContents(True)
#         self.updateFrameId()
#     
#     @pyqtSlot()
#     def playClicked(self):
#         self.paused = False
#         self.pausedbuffer = None  #NOTE: maybe we shouldn't clear it hear so they can record if after resuming.
#         self.ui.frameNum.setText("~")
#     
#     @pyqtSlot()
#     def nextClicked(self):
#         if self.paused and self.pausedbuffer:
#             frame = self.pausedbuffer.next()
#             if frame:
#                 self.ui.videoFrame.setPixmap(frame)
#                 self.ui.videoFrame.setScaledContents(True)
#                 self.updateFrameId()
#     
#     @pyqtSlot()
#     def backClicked(self):
#         if self.paused and self.pausedbuffer:
#             frame = self.pausedbuffer.prev()
#             if frame:
#                 self.ui.videoFrame.setPixmap(frame)
#                 self.ui.videoFrame.setScaledContents(True)
#                 self.updateFrameId()
#     
#     @pyqtSlot()
#     def recordClicked(self):
#         if self.pausedbuffer:
#             self.pausedbuffer.writeToDir("/tmp/video_%s" % time.strftime("%Y-%m-%d_%H-%M-%S"))
# 
#     def updateFrameId(self):
#         if self.pausedbuffer:
#             self.ui.frameNum.setText("%s/%s" % (self.pausedbuffer._frameidx + 1, len(self.pausedbuffer._frames)))
