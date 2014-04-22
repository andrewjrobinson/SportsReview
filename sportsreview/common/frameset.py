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

class FrameSet(object):
    '''Stores all frames at a single timepoint'''
    
    def __init__(self, timestamp=None):
        self._frames = []
        self.timestamp = timestamp
        
    def addFrame(self, frame):
        '''Adds a single frame to the frameset'''
        self._frames.append(frame)
    
    def __delitem__(self, key):
        self._frames.__delattr__(key)
    def __getitem__(self, key):
        return self._frames[key]
    def __len__(self):
        return len(self._frames)


class LazyFrameSet(object):
    '''Stores all frames at a single timepoint'''
    
    def __init__(self, timestamp=None, loadframefunc=None, loadframeopts=None):
        self.timestamp = timestamp
        self._loadframefunc = loadframefunc
        self._loadframeopts = loadframeopts
        self._frames = []
        self._framesloaded = []
        
    def addFrame(self, frame):
        '''Adds a single frame to the frameset'''
        self._frames.append(frame)
        self._framesloaded.append(False)
    
    def __delitem__(self, key):
        self._frames.__delattr__(key)
        self._framesloaded.__delattr__(key)
    def __getitem__(self, key):
        if not self._framesloaded[key]:
            self._frames[key] = self._loadframefunc(self, self._loadframeopts, self._frames[key])
            self._framesloaded[key] = True
        return self._frames[key]
    def __len__(self):
        return len(self._frames)
    