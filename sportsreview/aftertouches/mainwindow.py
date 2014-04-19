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
Created on 19/04/2014
@author: Andrew Robinson
'''

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot, pyqtSignal

import aftertouches, about

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self, settings, application=None):
        '''
        UI Object that draws the main window.
        
        Listens to the following settings:
        - delay: 
        '''
        QtGui.QWidget.__init__(self)
        self.ui = aftertouches.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.application = application
        
        self.aboutdlg = None
        
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.showAbout)
    
    @pyqtSlot()
    def showAbout(self):
        '''Slot to show the about dialog for the user'''
        if self.aboutdlg is None:
            self.aboutdlg = about.AboutDialog()
        self.aboutdlg.show()
    
# end class MainWindow
