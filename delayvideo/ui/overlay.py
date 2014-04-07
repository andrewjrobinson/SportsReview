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
Adds status messages on top of video streams.

Created on 26/03/2014

@author: arobinson
'''

import time

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot

class OverlayWidget(QtGui.QWidget):
    '''Draws messages over the video stream'''
    
    def __init__(self, parent = None, *args, **kwargs):
        QtGui.QWidget.__init__(self, parent, *args, **kwargs)
        self._messages = {}
        self.updateWidgetPosition()
        self.setFont(QtGui.QFont("Liberation Sans", 72)) #TODO: put font face in config file
        if parent is not None:
            #TODO: make sure it has a resized signal
            parent.resized.connect(self.parentResized)
        self._baseline = 0
        self._clearTimer = QtCore.QTimer(self)
        self._clearTimer.timeout.connect(self.clearTimeout);
        self._clearTimer.start(100);
    
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.Antialiasing = True
        self.drawWidget(qp)
        qp.end()
    
    def setParent(self, parent, *args, **kwargs):
        returncode = QtGui.QWidget.setParent(self, parent, *args, **kwargs)
        if parent is not None:
            #TODO: make sure it has a resized signal
            parent.resized.connect(self.parentResized())
        return returncode
    
    def drawWidget(self, qp):
        if None in self._messages:
            
            # outlined text
            #TODO: make the text colours into settings
            msg = self._messages[None][1]
            path = QtGui.QPainterPath()
            path.addText(QtCore.QPoint(1,self._baseline), self.font(), msg)
            qp.setPen(QtGui.QPen(QtCore.Qt.white, 1.5, QtCore.Qt.SolidLine))
            qp.setBrush(QtCore.Qt.black)
            qp.drawPath(path)
        
    def updateWidgetPosition(self):
        '''Resizes widget to content size and repositions within parent'''
        
        if None in self._messages:  #TODO: make this handle other groups
            self.show()
            pw = self.parent().childrenRect().width()
            ph = self.parent().childrenRect().height()
            
            # check size of content
            msg = self._messages[None][1]
            fm = QtGui.QFontMetrics(self.font())
            w = fm.width(msg)+2
            h = fm.height()+2
            self._baseline = fm.ascent()
            #TODO: make this scale the font size 
            
            # resize/position widget
            self.setGeometry((pw-w)/2,(ph-h)/2,w,h)
        else:
            self.hide()
        
    def addMessage(self, message, group=None):
        '''
        Adds a message to the overlay.  Only one message per group will be 
        displayed at once; a second one will override the first and update the 
        timeout for that group.
        
        @param message: string message to display
        @param group: groupname for message
        '''
        timeout = 1.5 # seconds, TODO: make this a setting
        
        self._messages[group] = (time.time() + timeout, message)
        self.updateWidgetPosition()
        
    @pyqtSlot()
    def clearTimeout(self):
        '''Clears the old messages'''
        now = time.time()
        keys = self._messages.keys()
        cleared = False
        for k in keys:
            if self._messages[k][0] < now:
                self._messages.pop(k)
                cleared = True
        if cleared:
            self.updateWidgetPosition()
        
    @pyqtSlot()
    def parentResized(self):
        '''Slot to receive parent resize events'''
        if len(self._messages) > 0:
            self.updateWidgetPosition()
        
# end class OverlayWidget
