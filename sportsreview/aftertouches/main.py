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
Created on 18/04/2014
@author: Andrew Robinson
'''
import sys

from PyQt4 import QtGui, QtCore
# from PyQt4.QtCore import pyqtSlot

import sportsreview.settings.settingsmanager
import mainwindow


class AfterTouchesApplication(QtCore.QObject):
    '''Performs the main logic/connections in the application'''
    
    def __init__(self, argv = [], parent=None):
        '''Performs the main logic/connections in the application'''
        
        QtCore.QObject.__init__(self, parent)
        
        # load settings file
        if len(argv) == 2:
            self.settings = sportsreview.settings.settingsmanager.SettingsManager(argv[1])
        else:
            self.settings = sportsreview.settings.settingsmanager.SettingsManager()
        
        # setup main window
        self.mainwindow = mainwindow.MainWindow(self.settings, self)
        self.mainwindow.show()
        
    def cleanup(self):
        '''Called just before closing application'''
        # save the settings (only if changed)
        if self.settings:
            self.settings.writeSettings()
# end class

def main(argv):
    
    args = argv[1:]
    args.insert(0, "After Touches")
    app = QtGui.QApplication(args)
    runtime = AfterTouchesApplication()
    rc = app.exec_()
    runtime.cleanup()
    sys.exit(rc)
 
if __name__ == '__main__':
    main(sys.argv)
