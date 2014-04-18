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
        self._current = 0
        self._currentset = False
        
        self._addcount = 0
        
    def addFrame(self, frame):
        '''
        Add a single frame to the group
        
        @param frame: a frame object
        '''
        #TODO: sanity check frame
        self._frames.append(frame)
        self._addcount += 1
        
    def addFrames(self, framelist, front=False, current=None):
        '''
        Add multiple frames at once.
        
        Note: current can be outside framelist's frames; it is just cliped the the range 
        of resulting framegroup.  i.e. it is the index relative to the start of framelist
        so can be +ve or -ve
        
        @param framelist: a list-like object containing the frames to add
        @param front: boolean, add frames to start of group rather then end
        @param current: int, update the current index to point to the specified frame within framelist
        '''
        if front:
            newframes = []
            newframes.extend(framelist)
            newframes.extend(self._frames)
            self._frames = newframes
            if current != None:
                self._current = current
                self._currentset = True
            elif self._currentset == True:
                self._current += len(framelist)
        else:
            if current != None:
                self._current = len(self._frames) + current
                self._currentset = True
            self._frames.extend(framelist)
            self._fixindex()
            
    def _fixindex(self):
        '''fixes the index'''
        if self._current < 0:
            self._current = 0
        elif self._current >= len(self._frames):
            self._current = max(0,len(self._frames)-1)
        
    def current(self):
        '''
        Retrieves the current frame
        
        @return: FrameSet, the current frameset
        '''
        try:
            return self._frames[self._current]
        except:
            return None
        
    def next(self):
        '''
        Moves to next frame (and returns the new frame)
        
        @return: FrameSet, the frameset in the next position
        '''
        self._current += 1
        if self._current >= len(self._frames):
            self._current = len(self._frames) - 1
        return self.current()
        
    def prev(self):
        '''
        Moves to previous frame (and returns the new frame)
        
        @return: FrameSet, the frameset in the previous position
        '''
        self._current -= 1
        if self._current < 0:
            self._current = 0
        return self.current()
        
    def index(self):
        '''
        Get the current frame number
        
        @return: int, the id of the current frame
        '''
        return self._current
    
    def __len__(self, *args, **kwargs):
        return len(self._frames)
    
    def __getitem__(self, k):
        return self._frames[k]
    
#end class FrameGroup
