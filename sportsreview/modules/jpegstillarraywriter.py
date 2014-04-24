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

import os
import time

from sportsreview.support.qtlib import QtCore, Slot

class JpegStillArrayWriter(QtCore.QObject):
    '''Writes a frame group to file in the form of 1 jpg per frameset per frame'''
    
    __CAPTURE_FRAME__ = False
    __PROCESS_FRAME__ = False
    __CAPTURE_GROUP__ = False
    __PROCESS_GROUP__ = True
    
    def __init__(self, settings, config):
        '''
        Writes a frame group to file in the form of 1 jpg per frameset per image
        
        @param settings: global settings object (from settings file)
        @param config: the specific configuration for this instance (from layout)
        '''
        QtCore.QObject.__init__(self)
        
        self._settings = settings
        self._config = config
        
        self._settings.settingChanged.connect(self.settingChanged)
        self._recorddirectory = settings.getSetting("recorddirectory")
    
    @classmethod
    def getModule(cls, settings, config):
        '''Returns an instance of this module for the provided settings'''
        return cls(settings, config)
    
    def processGroup(self, framegroup):
        '''
        Writes the frames within the frameset to disk as jpg images along with a summary text file
        
        @param framegroup: the incoming frame object
        '''
        
        if framegroup is not None:
            
            # calculate how many digits will be required
            digits = len(str(len(framegroup)))
            
            # make the output dir if needed
            outdir = "%s%svideo_%s" % (self._recorddirectory, os.path.sep, time.strftime("%Y-%m-%d_%H-%M-%S"), )
            if not os.path.exists(outdir):
                os.mkdir(outdir)
            
            idx = 1
            timingFile = open("%s%stiming.txt" % (outdir, os.path.sep), 'w')
            
            # write headers
            f0 = framegroup[0]
            startTimestamp = f0.timestamp
            timingFile.write("#timestamp=%s\n" % (startTimestamp,))
            timingFile.write("#frames=%s\n" % (len(framegroup),))
            timingFile.write("#streams=%s\n" % (len(f0),))
            
            # write frame files
            for frameset in framegroup:
                i = 0
                for frame in frameset:
                    filename = "%s%sframe-d%s-%s.jpg" % (outdir, os.path.sep, i, str(idx).zfill(digits))
                    timingFile.write("%s\t%s\t%s\t%s\n" % (idx-1, frameset.timestamp, i, filename,))
                    frame.asQPixmap().save(filename)
                    i+=1
                idx+=1
            
            timingFile.close()
            
            
        
    @Slot(str,object)
    def settingChanged(self, name, value):
        if name == "recorddirectory":
            self._recorddirectory = value
        
# end class JpegStillArrayWriter
