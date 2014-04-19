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

from sportsreview.support.qtlib import QtCore, Slot

class FrameDelay(QtCore.QObject):
    '''Delays the frames being processed for a set timeperiod'''
    
    __CAPTURE_FRAME__ = False
    __PROCESS_FRAME__ = True
    __CAPTURE_GROUP__ = False
    __PROCESS_GROUP__ = False
    
    def __init__(self, settings, config):
        '''
        Delays the frames being processed for a set timeperiod
        
        @param settings: global settings object (from settings file)
        @param config: the specific configuration for this instance (from layout)
        '''
        QtCore.QObject.__init__(self)
        
        self._settings = settings
        self._config = config
        
        self._settings.settingChanged.connect(self.settingChanged)
        self._delay = settings.getSetting("delay")
        
        self._frames = []
        self._lastframe = None
    
    @classmethod
    def getModule(cls, settings, config):
        '''Returns an instance of this module for the provided settings'''
        return cls(settings, config)
        
    def process(self, frame):
        '''
        Returns frame unchanged (but keeps a copy for configured timeperiod (settings file))
        
        @param frame: the incoming frame object
        @return: frame, the frame that was provided
        '''
        
        # store current frame
        self._frames.append(frame)
        
        # return a delayed one
        releasetime = frame.timestamp - self._delay
        getdata = None
        while len(self._frames) > 0:
            oframe = self._frames[0]
            if oframe.timestamp > releasetime:
                break
            self._lastframe = self._frames.pop(0)
        if self._lastframe:
            getdata = self._lastframe
        return getdata
    
    def giveFrames(self, framegroup):
        '''
        Get all the frames this module knows about which are used for pausing a video stream
        
        @param framegroup: the framegroup object to store frames in.
        '''
        
#         print "FrameDelay: %s frames" % len(self._frames)
        framegroup.addFrames(self._frames, current=0)
    
    @Slot(str,object)
    def settingChanged(self, name, value):
        if name == "delay":
            self._delay = float(value)

# 
# class FrameBuffer(QObject):
#     '''A buffer object to store frames (for a given timeperiod)'''
#     
#     
#     __CAPTURE_FRAME__ = False
#     __PROCESS_FRAME__ = True
#     __CAPTURE_GROUP__ = False
#     __PROCESS_GROUP__ = False
#     
#     
#     def __init__(self, settings):
#         '''
#         A buffer object to store frames (for a given timeperiod)
#         
#         Listens to settings object for changes to:
#         - delay: The amount of time (seconds) to delay frames from push() to get()
#         - keepalive: The amount of time (seconds) to keep frames after they are provided to get().  i.e. how much history for the pause function.
#         - extend: The amount of time (seconds) to keep recording frames for after pausing.
#         
#         @param settings: A settings manager instance which contains settings to use.
#         '''
#         
#         QObject.__init__(self)
#         
#         self.settings = settings
#         self.settings.settingChanged.connect(self.settingChanged)
#         self._delay = settings.getSetting("delay")
#         self._keepalive = settings.getSetting("keepalive")
#         self._extend = settings.getSetting("extend")
#         
#         self._frames = []       # the frames in the buffer
#         self._oldframes = []    # the recent old frames (for pause)
#         self.lastframe = None
#         self._clones = []       # list of clones that we are appending to still (i.e. paused buffers)
#     
#     class Frame(object):
#         '''A single frame'''
#         def __init__(self, timestamp, data):
#             self.timestamp = timestamp
#             self.data = data
#         
#     def push(self, framedata):
#         '''Add a frame to the buffer'''
#         ftime = time.time()
#         frame = self.Frame(ftime, framedata)
#         self._frames.append(frame)
#         
#         # extend clones and update list of incomplete clones
#         stillclones = []
#         for clone in self._clones:
#             if clone.addFrame(frame, ftime):
#                 stillclones.append(clone)
#         self._clones = stillclones
#         
#     def get(self):
#         '''Get the 'current' from from the buffer (based on delay)'''
#         releasetime = time.time() - self._delay
#         getdata = None
#         newframe = False
#         while len(self._frames) > 0:
#             frame = self._frames[0]
#             if frame.timestamp > releasetime:
#                 newframe = True
#                 break
#             self.lastframe = self._frames.pop(0)
#         if self.lastframe:
#             getdata = self.lastframe.data
#             
#             # keep old frames (for pause)
#             if self._keepalive > 0:
#                 if newframe: # only add it once
#                     self._oldframes.append(self.lastframe)
#                 
#                 # remove any expired oldframes
#                 releasetime -= self._keepalive # repurpose var
#                 while len(self._oldframes) > 0:
#                     frame = self._oldframes[0]
#                     if frame.timestamp > releasetime:
#                         break
#                     self._oldframes.pop(0)
#             
#         return getdata
#     
#     def getFrameRate(self):
#         '''Approximates frame-rate by comparing buffer size to delay'''
#         if self._delay > 0:
#             return len(self._frames) / self._delay
#         return 0
#     
#     @pyqtSlot(str,object)
#     def settingChanged(self, name, value):
#         if name == "delay":
#             self._delay = float(value)
#         elif name == "keepalive":
#             self._keepalive = float(value)
#         elif name == "extend":
#             self._extend = float(value)
#             
#     def cloneFrames(self):
#         '''Clones the frames in this buffer.  Note: buffer object will be 
#         returned immediately but added to later if length of buffer is 
#         insufficient'''
#         
#         clone = FrameList(self._frames, self._oldframes, time.time() + self._extend)
#         self._clones.append(clone)
#         return clone
#         
# 
# class FrameList(object):
#     '''A list of frames used when in paused mode'''
#     
#     def __init__(self, frames, oldframes, endtime):
#         '''
#         @param frames: a list of frames to shallow copy
#         @param oldframes: a list of old frames to shallow copy
#         @param endtime: float, the timestamp that this framelist should end, used to determine when to stop adding extra frames to this list
#         '''
#         self._frameidx = len(oldframes)
#         
#         self._frames = []
#         self._frames.extend(oldframes)
#         self._frames.extend(frames)
#         
#         self._endtime = endtime
#         if self._frameidx >= len(self._frames):
#             self._frameidx = len(self._frames) -1
# 
#         self._addframecount = 0
# #         print "frames: %s" % len(self._frames)
#         
#     def addFrame(self, frame, ftime):
#         '''Adds another frame to this buffer (after creation time)
#         @param frame: frame to add (though might reject it)
#         @param ftime: time when frame was captured
#         @return: boolean, False once a frame arrives after endtime
#         '''
#         if ftime > self._endtime:
# #             print "Added: %s frames" % self._addframecount
#             return False
#         self._addframecount += 1
#         self._frames.append(frame)
#         return True
#         
#     def next(self):
#         '''returns the next frame'''
#         self._frameidx += 1
#         if self._frameidx >= len(self._frames):
#             self._frameidx = len(self._frames) - 1
#             return None
#         return self._frames[self._frameidx].data
# 
#     def prev(self):
#         '''returns the previous frame'''
#         self._frameidx -= 1
#         if self._frameidx < 0 and self._frameidx < len(self._frames):
#             self._frameidx = 0
#             return None
#         return self._frames[self._frameidx].data
#     
#     def current(self):
#         '''returns the current frame'''
#         if self._frameidx < len(self._frames):
#             return self._frames[self._frameidx].data
#         return None
# 
#     def writeToDir(self, dir):
#         '''Writes each frame to a JPG file in provided dir
#         @param dir: string, directory name to write frames (files) too'''
#         
#         digits = len(str(len(self._frames))) # calculate how many digits will be required
#         if not os.path.exists(dir):
#             os.mkdir(dir)
#         
#         idx = 1
#         timingFile = open("%s%stiming.txt" % (dir, os.path.sep), 'w')
#         for frame in self._frames:
#             filename = "%s%sframe-%s.jpg" % (dir, os.path.sep, str(idx).zfill(digits))
#             timingFile.write("%s\t%s\n" % (frame.timestamp, filename,))
#             frame.data.save(filename)
#             idx+=1
#         
#         timingFile.close()
        
