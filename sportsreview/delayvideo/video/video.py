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
Created on 22/03/2014

@author: arobinson

Adapted from: http://wrdeoftheday.com/?page_id=2
'''

import cv2
import numpy as np
from PyQt4 import QtGui
 
class Video():
    def __init__(self,capture):
#         capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1920)
#         capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)
#         capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
#         capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 720)
        capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1024)
        capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 768)
#         capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
#         capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 320)
        self.capture = capture
        self.currentFrame=np.array([])
 
    def captureFrame(self):
        ret, readFrame=self.capture.read()
        if(ret==True):
            self.currentFrame=cv2.cvtColor(readFrame,cv2.COLOR_BGR2RGB)
 
    def convertFrame(self):
        try:
            height,width=self.currentFrame.shape[:2]
#             print "%s, %s" %(width, height)
            img=QtGui.QImage(self.currentFrame, width, height, QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None
