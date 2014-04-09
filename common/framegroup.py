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
Created on 09/04/2014
@author: Andrew Robinson
'''

import time

class FrameGroup(object):
    '''Stores a series of Frames'''
    
    def __init__(self, timestamp=None):
        '''
        Stores a series of Frames
        
        Note: FrameExtend uses timestamp to know how much longer to extend so
        for capture devices that record timestamps of an earlier capture this
        will need to be set to the time of the current frame
        
        @param timestamp: the timepoint within a framestream this group of frames was requested.
        '''
        self._frames = []
        if timestamp is None:
            timestamp = time.time()
        self.timestamp = timestamp
        
    def addFrame(self, frame):
        '''
        Add a single frame to the group
        
        @param frame: a frame object
        '''
        #TODO: sanity check frame
        self._frames.append(frame)
        
    def addFrames(self, framelist):
        '''
        Add multiple frames at once
        
        @param framelist: a list-like object containing the frames to add
        '''
        
        self._frames.extend(framelist)
        
#end class FrameGroup
