'''
Created on 22/03/2014

@author: arobinson
'''

import cv2
import numpy as np

from sportsreview.support.qtlib import QtGui

class Video():
    def __init__(self,capture):
        self.capture = capture
        self.currentFrame=np.array([])
 
    def captureFrame(self):
        """                                          
        capture frame and reverse RBG BGR and return opencv image                                                                         
        """
        ret, readFrame=self.capture.read()
        if(ret==True):
            self.currentFrame=cv2.cvtColor(readFrame,cv2.COLOR_BGR2RGB)
 
    def convertFrame(self):
        """
        converts frame to format suitable for QtGui
        """
        try:
            height,width=self.currentFrame.shape[:2]
            img=QtGui.QImage(self.currentFrame,
                              width,
                              height,
                              QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None
