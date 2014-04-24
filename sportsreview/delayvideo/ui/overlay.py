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
'''
Adds status messages on top of video streams.

Created on 26/03/2014

@author: arobinson
'''

import time

from sportsreview.support.qtlib import QtCore, QtGui, Slot

class OverlayWidget(QtGui.QWidget):
    '''Draws messages over the video stream'''
    
    def __init__(self, parent=None, settings=None, *args, **kwargs):
        QtGui.QWidget.__init__(self, parent, *args, **kwargs)
        self._settings = settings
        
        self._messages = {}
        self._messageorder = []
        self.setFont(QtGui.QFont("Liberation Sans", 72)) #TODO: put font face in config file
        if parent is not None:
            #TODO: make sure it has a resized signal
            parent.resized.connect(self.parentResized)
        self._baseline = 0
        self._clearTimer = QtCore.QTimer(self)
        self._clearTimer.timeout.connect(self.clearTimeout);
        self._clearTimer.start(100);
        
        self.updateWidgetPosition()
    # end __init__()
    
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
            i = 0
            for group in self._messageorder:
                msg = self._messages[group][1]
                msgpos = self._msgposs[i]
                path = QtGui.QPainterPath()
                path.addText(QtCore.QPoint(*msgpos), self.font(), msg)
                qp.setPen(QtGui.QPen(QtCore.Qt.white, 1.5, QtCore.Qt.SolidLine))
                qp.setBrush(QtCore.Qt.black)
                qp.drawPath(path)
                i += 1
        
    def updateWidgetPosition(self):
        '''Resizes widget to content size and repositions within parent'''
        
        if len(self._messages) > 0:
            self.show()
            pw = self.parent().childrenRect().width()
            ph = self.parent().childrenRect().height()
            
            # check size of each message
            w = 0
            h = 0
            fm = QtGui.QFontMetrics(self.font())
            msgposs = []
            for group in self._messageorder:
                msg = self._messages[group][1]
                mw = fm.width(msg)+2
                msgposs.append((mw,h + fm.ascent()))
                w = max(w,mw)
                h += fm.height()+2
                #TODO: make this scale the font size
            
            # calculate the left positions
            self._msgposs = []
            for msgpos in msgposs:
                self._msgposs.append(((w-msgpos[0])/2 ,msgpos[1]))
            
            # resize/position widget
            self.setGeometry((pw-w)/2,(ph-h)/2,w,h)
            
            # refresh the screen
            self.update()
        else:
            self.hide()
        
    def addMessage(self, message, group=None, timeout=1.5):
        '''
        Adds a message to the overlay.  Only one message per group will be 
        displayed at once; a second one will override the first and update the 
        timeout for that group.
        
        @param message: string message to display
        @param group: groupname for message
        @param timeout: the amount of seconds to keep message showing
        '''
        #TODO: make timeout default to a setting value
        
        self._messages[group] = (time.time() + timeout, message)
        
        # save the ordering of messages
        if group in self._messageorder:
            self._messageorder.remove(group)
        self._messageorder.append(group)
        
        # update position
        self.updateWidgetPosition()
        
    @Slot()
    def clearTimeout(self):
        '''Clears the old messages'''
        now = time.time()
        keys = self._messages.keys()
        cleared = False
        for k in keys:
            if self._messages[k][0] < now:
                self._messages.pop(k)
                if k in self._messageorder:
                    self._messageorder.remove(k)
                cleared = True
        if cleared:
            self.updateWidgetPosition()
        
    @Slot()
    def parentResized(self):
        '''Slot to receive parent resize events'''
        if len(self._messages) > 0:
            self.updateWidgetPosition()
        
# end class OverlayWidget
