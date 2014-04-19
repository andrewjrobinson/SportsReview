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

from sportsreview.support.qtlib import QtCore, QtGui, Slot, Signal

import aftertouches, about

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self, settings, application=None):
        '''
        UI Object that draws the main window.
        
        Listens to the following settings:
        - delay: 
        '''
        QtGui.QMainWindow.__init__(self)
        self.ui = aftertouches.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.application = application
        
        self.settings = settings
        self.settings.settingChanged.connect(self.settingChanged)
        
        self._windowstate = None
        self.aboutdlg = None
        
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.showAbout)
        self.ui.actionOpen.triggered.connect(self.openFileDialog)
        
        self._bindings = {}
        self._loadBindings(settings.getSetting('keybinding'))
    #end init()
    
    ## Signals ##
    openfile = Signal(str)
    
    ## Slots ##
    @Slot(str,object)
    def settingChanged(self, name, value):
        if name == "keybinding":
            self._loadBindings(value)
            
    @Slot()
    def showAbout(self):
        '''Slot to show the about dialog'''
        if self.aboutdlg is None:
            self.aboutdlg = about.AboutDialog()
        self.aboutdlg.show()
    
    @Slot()
    def openFileDialog(self):
        '''
        Slot to ask user for a (video) file
        '''
        # get the file from the user
        filename = QtGui.QFileDialog.getOpenFileName(self, 
                     self.tr("Open recording"), 
                     str(self.settings.getSetting("recorddirectory")), 
                     self.tr("Video Files (*.txt)"))
        
        if filename[0] != '':
            self.ui.statusBar.showMessage("Opening %s" % (filename[0],))
            
            # tell app to open the file
            self.openfile.emit(filename[0])
    
    ## reimplemented
    def showEvent(self, *args, **kwargs):
        if self._windowstate is None:
            self._windowstate = self.settings.getSetting("aftertouchesui")
            self.setGeometry(*self._windowstate['geometry'])
            if self._windowstate['mode'] == 'fullscreen':
                self.showFullScreen()
            elif self._windowstate['mode'] == 'maximised':
                self.showMaximized()
        return QtGui.QMainWindow.showEvent(self, *args, **kwargs)
    
    def closeEvent(self, *args, **kwargs):
        if self._windowstate is not None:
            self._windowstate = self.settings.getSetting("aftertouchesui")
            if self._windowstate['savemode'] == True:
                if self.windowState() == QtCore.Qt.WindowFullScreen:
                    self._windowstate['mode'] = "fullscreen"
                elif self.windowState() == QtCore.Qt.WindowMaximized:
                    self._windowstate['mode'] = "maximised"
                else:
                    self._windowstate['mode'] = "normal"
            if self._windowstate['savegeometry'] == True:
                self._windowstate['geometry'] = self.geometry().getRect()
            self.settings.setSetting('aftertouchesui', self._windowstate)
        
        return QtGui.QMainWindow.closeEvent(self, *args, **kwargs)
    
    def keyPressEvent(self, e):
        '''Perform tasks for various key events'''
        
        if e.key() in self._bindings:
            for binding in self._bindings[e.key()]:
                func, action, config = binding
                func(action, config)
        else:
            print "key: %s" % (e.key(),)
    
    ## Other APIs ##
    def setStatusMsg(self, msg, timeout=0):
        '''
        Set the status bar message
        
        @param msg: the message to display
        @param timeout: the length of time to leave message (millisec), default no timeout
        '''
        self.ui.statusBar.showMessage(msg, timeout)
    
    def toggleFullScreen(self):
        '''Toggles between fullscreen and normal mode'''
        if not self.isFullScreen():
            self.showFullScreen()
        else:
            self.showNormal()
    
    ## Support ##
    def _loadBindings(self, bindings):
        '''
        Extracts the actual key ids from the string representations of them provided.
        
        @param bindings: dict containing keybindings {'<keyname>': [('<group>', '<function>', <optionargs>,...), ...]} 
        '''
        try:
            
            groups = {'core': 'core',
#                     'processframe': lambda m,c: self.processFrame.emit(m,c),
#                     'processgroup': lambda m,c: self.processGroup.emit(m,c),
                    }
            corefuncs = {
                         'quit': lambda a,b: self.close(),
#                          'play': lambda a,b: self.togglePlay.emit(),
#                          'incdelay': lambda a,b: self.incDelay.emit(),
#                          'decdelay': lambda a,b: self.decDelay.emit(),
#                          'incframe': lambda a,b: self.incFrame.emit(),
#                          'decframe': lambda a,b: self.decFrame.emit(),
                         'fullscreen': lambda a,b: self.toggleFullScreen(),
#                          'edit': lambda a,b: self.edit.emit(),
#                          'help': lambda a,b: self.help.emit(),
                         }
            
            errors = []
            self._bindings = {}
            for keystr, events in bindings.items():
                for event in events:
                    try:
                        # convert to integer
                        keyint = getattr(QtCore.Qt,"Key_%s"% str(keystr))
                        
                        # get functions to perform tasks
                        func = None
                        try: func = groups[event[0]]
                        except KeyError: pass
                        if func == 'core':
                            try: func = corefuncs[event[1]]
                            except KeyError: pass
                        
                        if func is not None and func is not 'core':
                            if keyint in self._bindings:
                                self._bindings[keyint].append((func, event[1], event[2:]))
                            else:
                                self._bindings[keyint] = [(func, event[1], event[2:])]
                    except AttributeError:
                        errors.append("Key: %s" %keystr)
                    except KeyError:
                        errors.append("Group: %s" %keystr)

            if len(errors) > 0:
                print "Ignoring the following invalid key bindings (%s)" % (", ".join(errors)) 
        except:
            pass
    
# end class MainWindow
