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
import types
'''
Responsible for loading and saving settings and issuing signals when changes occur

Created on 26/03/2014

@author: arobinson
'''

import os

from PyQt4.QtCore import pyqtSignal, QObject

import sportsreview.support

class SettingsManager(QObject):
    '''Loads, updates and writes settings from/to disk'''

    def __init__(self, settingsfilename=None):
        '''Loads a specific settings file (or default one)'''
        
        QObject.__init__(self)
        
        if settingsfilename is not None and os.path.exists(settingsfilename):
            self._settingsfilename = settingsfilename
        else:
            self._settingsfilename = "%s/settings.py" % os.path.dirname(__file__)
        
        settingsmodule = sportsreview.support.loadModule('delayvideo.settings', self._settingsfilename)
        
        self._settings = settingsmodule.settings
        self._docstring = settingsmodule.__doc__
        try:
            if isinstance(settingsmodule.__order__, types.ListType):
                self._order = settingsmodule.__order__
            else:
                self._order = []
        except:
            self._order = []
        self._dirty = False
        
    # end __init__()

    settingChanged = pyqtSignal(str, object) # name, value
        
    def writeSettings(self, force=False):
        '''Write the settings back to the file (if needed)'''
        if self._dirty or force:
            f = open(self._settingsfilename, 'w')
            if f:
                f.write("'''%s'''\n" % self._docstring)
                f.write("settings = %s\n" % self.formatDict(self._settings))
                f.write("__order__= %s\n" % self._order)
                self._dirty = False
                f.close()
                return True
            return False
        return True
    
    def formatDict(self, d, depth=0):
        '''Returns a formatted dict (as string)'''
        try:
            # calculate the order of dict keys
            if depth == 0:
                missing = [x for x in d if x not in self._order]
                keys = [x for x in self._order if x in d]
                keys.extend(missing)
                self._order = keys
            else:
                keys = d.keys()
                keys.sort()
            
            # print each element of dict
            output = "{\n"
            for k in keys:
                v = d[k]
                output += "\t" * (depth + 1)
                if isinstance(v, (types.DictType)):
                    output += "'%s': %s,\n" % (k,self.formatDict(v, depth+1))
                elif isinstance(v, (types.ListType)):
                    output += "'%s': %s,\n" % (k,self.formatList(v, depth+1))
                elif isinstance(v, (types.StringType)):
                    output += "'%s': '%s',\n" % (k,v)
                else:
                    output += "'%s': %s,\n" % (k,v)
            output += "\t" * depth
            output += "}"
            return output
        except:
            return str(d)
    
    def formatList(self, l, depth):
        '''Returns a formatted list (as string)'''
        try:
            output = "[\n"
            for v in l:
                output += "\t" * (depth + 1)
                if isinstance(v, (types.DictType)):
                    output += "%s,\n" % (self.formatDict(v, depth+1),)
                elif isinstance(v, (types.ListType)):
                    output += "%s,\n" % (self.formatList(v, depth+1),)
                elif isinstance(v, (types.StringType)):
                    output += "'%s',\n" % (v,)
                else:
                    output += "%s,\n" % (v,)
            output += "\t" * depth
            output += "]"
            return output
        except:
            return str(l)
    def getSetting(self, name):
        try:
            return self._settings[name]
        except:
            return None
    
    def setSetting(self, name, value):
        if name in self._settings:
            self._settings[name] = value
            self._dirty = True
            self.settingChanged.emit(name, value)
            return True
        return False
    
