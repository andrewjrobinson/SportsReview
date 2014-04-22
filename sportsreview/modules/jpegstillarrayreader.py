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
from sportsreview.common.frameset import LazyFrameSet
'''
Created on 22/04/2014
@author: Andrew Robinson

A companion reader to 'recordstillcv' module.  Used by AfterTouches to read a 
previously recorded FrameGroup 
'''

from sportsreview.support.qtlib import QtCore, QtGui

from sportsreview.common.framegroup import LazyFrameGroup

class JpegStillArrayReader(QtCore.QObject):
    '''Reads a frame group from file in the form of 1 jpeg per frameset per image'''
    
    __CAPTURE_FRAME__ = False
    __PROCESS_FRAME__ = False
    __CAPTURE_GROUP__ = True
    __PROCESS_GROUP__ = False

    def __init__(self, settings, config):
        '''
        Reads a frame group from file in the form of 1 jpeg per frameset per image
        
        @param settings: global settings object (from settings file)
        @param config: the specific configuration for this instance (from layout)
        '''
        QtCore.QObject.__init__(self)
        
        self._settings = settings
        self._config = config

    @classmethod
    def getModule(cls, settings, config):
        '''Returns an instance of this module for the provided settings'''
        return cls(settings, config)
    
    def load(self, options):
        '''
        Loads a file.
        
        @param options: dictionary, expects key 'filename'
        @return: FrameGroup like object
        '''
        def lazysetloader(sself, _, framefilename):
#             print "Loading: %s" % framefilename
            pmap = QtGui.QPixmap(framefilename)
            return pmap
        def lazygrouploader(gself, timingfilename):
            f = open(timingfilename)
            result = []
            for line in f:
                cols = line.strip().split('\t')
                
                # get the frameset (or create new one)
                try:
                    fset = result[int(cols[0])]
                except IndexError:
                    result.append(LazyFrameSet(timestamp=cols[1], loadframefunc=lazysetloader))
                    fset = result[int(cols[0])]
                
                # add the frame file to it
                fset.addFrame(cols[3]) #TODO: make frameset support stream id's (so we can handle missing frames)
            return result
        
        return LazyFrameGroup(None, lazygrouploader, options['filename'])


  
#end class JpegStillArrayReader
    
    