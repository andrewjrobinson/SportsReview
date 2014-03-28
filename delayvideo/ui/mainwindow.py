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
    
    def __init__(self, settings, application=None):
        '''
        UI Object that draws the main window.
        
        Listens to the following settings:
        - delay: 
        '''
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update()
        self.application = application
        
        self.settings = settings
        self.settings.settingChanged.connect(self.settingChanged)
        self.ui.delay.setText(str(settings.getSetting("delay")))
        
    # end __init__()
    
    # signals
    incDelay = pyqtSignal()         #+>=. (while running)
    decDelay = pyqtSignal()         #-<,  (while running)
    incFrame = pyqtSignal()         #+>=. (while paused)
    decFrame = pyqtSignal()         #-<,  (while paused)
    help = pyqtSignal()             #F1
    edit = pyqtSignal()             #F2
    togglePlay = pyqtSignal()       #F7 <space>
    recordBuffer = pyqtSignal()     #F12
    
    
    @pyqtSlot()
    def settingChanged(self, name, value):
        if name == "delay":
            self.ui.delay.setText(value)
        
    
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
