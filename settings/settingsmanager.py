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
Responsible for loading and saving settings and issuing signals when changes occur

Created on 26/03/2014

@author: arobinson
'''

import os

from PyQt4.QtCore import pyqtSignal, QObject

import support

class SettingsManager(QObject):
    '''Loads, updates and writes settings from/to disk'''

    def __init__(self, settingsfilename=None):
        '''Loads a specific settings file (or default one)'''
        
        QObject.__init__(self)
        
        if settingsfilename is not None and os.path.exists(settingsfilename):
            self._settingsfilename = settingsfilename
        else:
            self._settingsfilename = "%s/settings.py" % os.path.dirname(__file__)
        
        settingsmodule = support.loadModule('delayvideo.settings', self._settingsfilename)
        
        self._settings = settingsmodule.settings
        self._docstring = settingsmodule.__doc__
        self._dirty = False
        
    # end __init__()

    settingChanged = pyqtSignal() # name, value
        
    def writeSettings(self, force=False):
        '''Write the settings back to the file (if needed)'''
        if self._dirty or force:
            f = open(self._settingsfilename, 'w')
            if f:
                f.write("'''%s'''\n" % self._docstring)
                f.write("settings = %s\n" % self._settings)
                self._dirty = False
                f.close()
                return True
            return False
        return True
        
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
    
