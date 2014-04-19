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
Created on 08/04/2014
@author: Andrew Robinson
'''

import cv2

from sportsreview.support.qtlib import QtGui

class UsbCamCaptureCV(object):
    '''A module that captures frames from usb camera's (via OpenCV)'''
    
    # Tell sports review what type of module we are
    __CAPTURE_FRAME__ = True
    __PROCESS_FRAME__ = False
    __CAPTURE_GROUP__ = False
    __PROCESS_GROUP__ = False
    
    def __init__(self, settings, config):
        '''
        A module that captures frames from usb camera's (via OpenCV)
        
        @param settings: global settings object (from settings file)
        @param config: the specific configuration for this instance (from layout)
        '''
        self.settings = settings
        self.config = config
        self._last = None
        try:
            self.cam = cv2.VideoCapture(config[0])
        except:
            pass

    def getFrame(self):
        '''Returns a single (current) frame from the device'''
        status, rawdata =  self.cam.read()
        if status:
            self._last = rawdata
            return CVFrame(rawdata)
        elif self._last is not None:
            return CVFrame(self._last)
        else:
            return CVFrame(None)
    
    @classmethod
    def getModule(cls, settings, config):
        '''Returns an instance of this module for the provided settings'''
        return cls(settings, config)
    
    @classmethod
    def enumerateDevices(cls):
        '''Returns a list of devices available'''
        devices = []
        i = 0
        while True:
            cam = cv2.VideoCapture(i)
            if not cam.isOpened():
                break
            cam.release()
            devices.append((i, "Cam %s" % i))
            i += 1

#end class UsbCamCaptureCV
     
class CVFrame(object):
    '''Stores a frame from the CV Capture device'''
    
    def __init__(self, rawdata):
        if rawdata is not None:
            self._rgbdata = cv2.cvtColor(rawdata,cv2.COLOR_BGR2RGB)
        else:
            self._rgbdata = None
        
    def asQPixmap(self):
        '''Returns a qpixmap for this frame'''
        if self._rgbdata is not None:
            height,width=self._rgbdata.shape[:2]
            qimg=QtGui.QImage(self._rgbdata, width, height, QtGui.QImage.Format_RGB888)
        else:
            qimg=QtGui.QImage(320, 240, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(qimg)
        
    def asQImage(self):
        '''Returns a qimage version of this frame'''
        height,width=self._rgbdata.shape[:2]
        return QtGui.QImage(self._rgbdata, width, height, QtGui.QImage.Format_RGB888)

# end class CVFrame
