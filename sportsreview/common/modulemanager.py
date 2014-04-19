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
Created on 08/04/2014
@author: Andrew Robinson
'''
import inspect

import sportsreview.modules

class ModuleManager(object):
    '''lists available module classes for type'''
    _captureframemodules = None
    _processframemodules = None
    _processgroupmodules = None
    
    @classmethod
    def getCaptureFrameModules(cls, refresh=True):
        '''Gets a list of all capture frame modules (class)'''
        if refresh or cls._captureframemodules is None:
            cls._captureframemodules = {}
            pymods = [sportsreview.modules.__dict__.get(a) for a in dir(sportsreview.modules)  if inspect.ismodule(sportsreview.modules.__dict__.get(a))]
            for pymod in pymods:
                for name in dir(pymod):
                    obj = getattr(pymod, name, None)
                    if inspect.isclass(obj):
                        try:
                            if obj.__CAPTURE_FRAME__ == True:
                                cls._captureframemodules[str(name)] = obj
                        except:
                            pass
        return cls._captureframemodules.values()

    @classmethod
    def getCaptureFrameModule(cls, name):
        '''Gets a single capture frame module by name'''
        
        cls.getCaptureFrameModules(False)
        return cls._captureframemodules[str(name)]
    
    @classmethod
    def getProcessFrameModules(cls, refresh=True):
        '''Gets a list of all Process frame modules (class)'''
        if refresh or cls._processframemodules is None:
            cls._processframemodules = {}
            pymods = [sportsreview.modules.__dict__.get(a) for a in dir(sportsreview.modules)  if inspect.ismodule(sportsreview.modules.__dict__.get(a))]
            for pymod in pymods:
                for name in dir(pymod):
                    obj = getattr(pymod, name, None)
                    if inspect.isclass(obj):
                        try:
                            if obj.__PROCESS_FRAME__ == True:
                                cls._processframemodules[str(name)] = obj
                        except:
                            pass
        return cls._processframemodules.values()

    @classmethod
    def getProcessFrameModule(cls, name):
        '''Gets a single Process frame module by name'''
        
        cls.getProcessFrameModules(False)
        return cls._processframemodules[str(name)]
    
    @classmethod
    def getProcessGroupModules(cls, refresh=True):
        '''Gets a list of all Process group modules (class)'''
        if refresh or cls._processgroupmodules is None:
            cls._processgroupmodules = {}
            pymods = [sportsreview.modules.__dict__.get(a) for a in dir(sportsreview.modules)  if inspect.ismodule(sportsreview.modules.__dict__.get(a))]
            for pymod in pymods:
                for name in dir(pymod):
                    obj = getattr(pymod, name, None)
                    if inspect.isclass(obj):
                        try:
                            if obj.__PROCESS_GROUP__ == True:
                                cls._processgroupmodules[str(name)] = obj
                        except:
                            pass
        return cls._processgroupmodules.values()

    @classmethod
    def getProcessGroupModule(cls, name):
        '''Gets a single Process group module by name'''
        
        cls.getProcessGroupModules(False)
        return cls._processgroupmodules[str(name)]
