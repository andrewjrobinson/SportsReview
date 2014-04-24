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
Created on 24/04/2014
@author: Andrew Robinson
'''
import numpy as np
import os, time
import cv2
from cv2 import cv

from sportsreview.support.qtlib import QtCore, QtGui, Slot

class AviWriterCV(QtCore.QObject):
    '''Writes frames from specified stream of framegroup to an AVI file using OpenCV'''
    
    __CAPTURE_FRAME__ = False
    __PROCESS_FRAME__ = False
    __CAPTURE_GROUP__ = False
    __PROCESS_GROUP__ = True
    
    def __init__(self, settings, config):
        '''
        Writes frames from specified stream of framegroup to an AVI file using OpenCV
        
        @param settings: global settings object (from settings file)
        @param config: the specific configuration for this instance (from layout)
        '''
        QtCore.QObject.__init__(self)
        
        self._settings = settings
        self._stream = config[0]
        
        self._settings.settingChanged.connect(self.settingChanged)
        self._recorddirectory = settings.getSetting("recorddirectory")
    
    @classmethod
    def getModule(cls, settings, config):
        '''Returns an instance of this module for the provided settings'''
        return cls(settings, config)
    
    def processGroup(self, framegroup):
        '''
        Writes frames from specified stream of framegroup to an AVI file using OpenCV
        
        @param framegroup: the incoming framegroup object
        '''
        
        if framegroup is not None:
            ext = "avi"
            codec = "DIVX"
            # calculate details
            fps = int(round(len(framegroup) / (framegroup[-1].timestamp - framegroup[0].timestamp)))
            f0 = framegroup[0][self._stream].asQImage()
            fsize = (f0.width(),f0.height())
            filename = framegroup.filename
            if filename is None:
                filename = "%s%svideo_%s" % (self._recorddirectory, os.path.sep, time.strftime("%Y-%m-%d_%H-%M-%S"), )
            filename += ".%s" % ext
            
            # open writer
            writer = cv2.VideoWriter(filename,cv.CV_FOURCC(*codec),fps,fsize)
            
            # write frame files
            for frameset in framegroup:
                frame = self._QImageToCv(frameset[self._stream].asQImage())
                writer.write(frame)
            
        
    @Slot(str,object)
    def settingChanged(self, name, value):
        if name == "recorddirectory":
            self._recorddirectory = value



    def _QImageToCv(self,img):
        '''Convert QImage to OpenCV image format'''
        img = img.convertToFormat(QtGui.QImage.Format.Format_RGB32)
        nparr = np.array(img.constBits()).reshape(img.height(), img.width(), 4)
        nparr = np.delete(nparr, 3, 2)
        return nparr

# end class JpegStillArrayWriter