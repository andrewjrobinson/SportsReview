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
Created on 10/04/2014
@author: Andrew Robinson
'''

from sportsreview.support.qtlib import QtCore, QtGui, Slot


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class RenderWidget(QtGui.QLabel):
    '''Draws frames from video stream'''
    
    def __init__(self, parent = None, *args, **kwargs):
        '''
        Draws frames from video stream
        
        @param parent: QWidget, the parent widget of this.
        '''
        QtGui.QLabel.__init__(self, parent, *args, **kwargs)
        self.hide() # hidden until it receives a layout
        self._streamid = None
        self._positions = None
        self._scaleparams = None
        self._copyparams = None
        
        if parent is not None:
            #TODO: make sure it has a resized signal
            parent.resized.connect(self.parentResized)
    
#     def paintEvent(self, e):
#         qp = QtGui.QPainter()
#         qp.begin(self)
#         qp.Antialiasing = True
#         self.drawWidget(qp)
#         qp.end()
    
    def setParent(self, parent, *args, **kwargs):
        returncode = QtGui.QWidget.setParent(self, parent, *args, **kwargs)
        if parent is not None:
            #TODO: make sure it has a resized signal
            parent.resized.connect(self.parentResized())
        return returncode
    
    def setLayout(self, layout):
        '''
        Layout the renderwidget in desired manner
        
        <streamid>: the frame to render (within a frameset)
        <top>, <left>, <bottom>, <right>: a double 0 = top of screen, 1 = bottom
        
        @param layout: 5-tuple, (<streamid>, <top>, <left>, <bottom>, <right>)
        '''
        self._streamid = layout[0]
        self._positions = layout[1:]
        self.updateWidgetPosition()
    
#     def drawWidget(self, qp):
#         if None in self._messages:
#             
#             # outlined text
#             #TODO: make the text colours into settings
#             msg = self._messages[None][1]
#             path = QtGui.QPainterPath()
#             path.addText(QtCore.QPoint(1,self._baseline), self.font(), msg)
#             qp.setPen(QtGui.QPen(QtCore.Qt.white, 1.5, QtCore.Qt.SolidLine))
#             qp.setBrush(QtCore.Qt.black)
#             qp.drawPath(path)
        
    def updateWidgetPosition(self):
        '''Resizes widget to content size and repositions within parent'''
        
        if self._streamid is not None:
            # load the icon if we are coming out of hidden state
            if self.isHidden():
                self.setPixmap(QtGui.QPixmap(_fromUtf8(":/common/resources/icon.svg")))
                self.setAlignment(QtCore.Qt.AlignCenter)
                self.show()
                
            # get area we have to play with
            ps = self.parent().size()
            pw = ps.width()
            ph = ps.height()
            
            # compute size
            top = ph * self._positions[0]
            left = pw * self._positions[1]
            bottom = ph * self._positions[2]
            right = pw * self._positions[3]
            
            # resize/position widget
            self.setGeometry(left, top, right-left, bottom-top)
            
            # recalc transforms
            self._scaleparams = None
            self._copyparams = None
            
            # refresh the screen
            self.update()
        else:
            self.hide()
    
    def process(self, frameset):
        '''
        Render the frame onto the component
        
        @param frameset: FrameSet, render the selected stream from here
        '''
        
        if self._streamid is not None:
            frame = frameset[self._streamid]
            if frame is not None:
                pm = frame.asQPixmap()
                
                # calculate (and cache) transformation params
                if self._scaleparams is None:
                    pw = pm.width()
                    ph = pm.height()
                    mw = self.width()
                    mh = self.height()
                    
                    # scale for clipping
                    pwn = (mh * pw) / ph 
                    phn = mh
                    pxn = (pwn - mw) / 2
                    pyn = 0
                    if pwn < mw:
                        pwn = mw
                        phn = (mw * ph) / pw
                        pxn = 0
                        pyn = (phn - mh) / 2
                    self._scaleparams = (pwn, phn)
                    self._copyparams = (pxn, pyn, mw, mh)
#                     print "Scale: %sx%s Crop: %sx%s %sx%s" % (pwn, phn, pxn, pyn, mw, mh)
                
                pmn = pm.scaled(*(self._scaleparams)) # size to cover fully
                pmn = pmn.copy(*(self._copyparams)) # crop excess
                
                self.setPixmap(pmn)
        
    @Slot()
    def parentResized(self):
        '''Slot to receive parent resize events'''
        self.updateWidgetPosition()
        
# end class OverlayWidget

