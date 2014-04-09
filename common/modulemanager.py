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
Created on 08/04/2014
@author: Andrew Robinson
'''
import inspect
import types

import modules

class ModuleManager(object):
    '''lists available module classes for type'''
    _modules = None
    
    @classmethod
    def getCaptureFrameModules(cls, refresh=True):
        '''Gets a list of all capture frame modules (class)'''
        if refresh or cls._modules is None:
            cls._modules = {}
            pymods = [modules.__dict__.get(a) for a in dir(modules)  if inspect.ismodule(modules.__dict__.get(a))]
            for pymod in pymods:
                for name in dir(pymod):
                    obj = getattr(pymod, name, None)
                    if inspect.isclass(obj):
                        try:
                            if obj.__CAPTURE_FRAME__ == True:
                                cls._modules[name] = obj
                        except:
                            pass
        return cls._modules.values()

    @classmethod
    def getCaptureFrameModule(cls, name):
        '''Gets a single capture frame module by name'''
        
        cls.getCaptureFrameModules(False)
        return cls._modules[name]
