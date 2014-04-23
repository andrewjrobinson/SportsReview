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
    
    def peekNext(self):
        '''
        Similar to next() except doesn't move current position
        '''
        try:
            return self._frames[self._current + 1]
        except:
            return None
    
    def peekPrev(self):
        '''
        Similar to prev() except doesn't move current position
        '''
        try:
            return self._frames[self._current - 1]
        except:
            return None
            
    
    def setPosition(self, idx):
        '''
        Moves to the specified index.
        @param idx: int, the index to set the 'current' to
        '''
        self._current = idx
        self._fixindex()
        
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

class LazyFrameGroup(object):
    '''
    Stores frames like a FrameGroup except the data is only loaded on need
    '''
    
    def __init__(self, timestamp=None, loadframelistfunc=None, loadframelistopts=None ):
        '''
        Stores frames like a FrameGroup except the data is only loaded on need
        
        loadframelistfunc params: func passed must have following params
        - self: LazyFrameGroup, the object that this frame is a part of.
        - opts: object, the value passed in constructor (loadframelistopts)
        
        @param timestamp: double, the time when this framegroup was created
        @param loadframelistfunc: callable, called when the framegroup needs to first know how many frames exist
        @param loadframelistopts: object, a value passed to func when called
        '''
        
        self._frames = None
        if timestamp is None:
            timestamp = time.time()
        self.timestamp = timestamp
        self._loadframelistfunc = loadframelistfunc
        self._loadframelistopts = loadframelistopts
        self._current = 0
        self._currentset = False
        
    def current(self):
        '''
        Retrieves the current frame
        
        @return: FrameSet, the current frameset
        '''
        self._loadframeinfo()
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
    
    def peekNext(self):
        '''
        Similar to next() except doesn't move current position
        '''
        self._loadframeinfo()
        try:
            return self._frames[self._current + 1]
        except:
            return None
    
    def peekPrev(self):
        '''
        Similar to prev() except doesn't move current position
        '''
        self._loadframeinfo()
        try:
            return self._frames[self._current - 1]
        except:
            return None
    
    def setPosition(self, idx):
        '''
        Moves to the specified index.
        @param idx: int, the index to set the 'current' to
        '''
        self._current = idx
        self._fixindex()
    
    def index(self):
        '''
        Get the current frame number
        
        @return: int, the id of the current frame
        '''
        return self._current
    
    def __len__(self, *args, **kwargs):
        self._loadframeinfo()
        return len(self._frames)
    
    def __getitem__(self, k):
        self._loadframeinfo()
        return self._frames[k]
    
    ## support ##
    def _fixindex(self):
        '''fixes the index'''
        if self._current < 0:
            self._current = 0
        elif self._current >= len(self._frames):
            self._current = max(0,len(self._frames)-1)
    
    def _loadframeinfo(self):
        if self._frames is None:
            self._frames = self._loadframelistfunc(self, self._loadframelistopts)

# end class LazyFrameGroup
