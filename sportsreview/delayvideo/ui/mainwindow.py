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
Creates and manages the main window from the ui.py file

Created on 26/03/2014

@author: arobinson
'''

from sportsreview.support.qtlib import QtCore, QtGui, Slot, Signal

from ui import Ui_MainWindow
from sportsreview.delayvideo.ui.render import RenderWidget


class MainWindow(QtGui.QMainWindow):
    
    def __init__(self, settings, application=None):
        '''
        UI Object that draws the main window.
        
        Listens to the following settings:
        - delay: 
        '''
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self._renderwidgets = [
                               RenderWidget(self),
                               RenderWidget(self),
                               RenderWidget(self),
                               RenderWidget(self),
                               ]
        
        self.update()
        self.application = application
        
        self.settings = settings
        self.settings.settingChanged.connect(self.settingChanged)
        self.ui.delay.setText(str(settings.getSetting("delay")))
        self._loadScreens(self.settings.getSetting("layouts")[self.settings.getSetting("selectedlayout")]["screen"])
        self._bindings = {}
        self._loadBindings(settings.getSetting('keybinding'))
        
    # end __init__()
    
    # signals
    incDelay = Signal()         #+>=. (while running)
    decDelay = Signal()         #-<,  (while running)
    incFrame = Signal()         #+>=. (while paused)
    decFrame = Signal()         #-<,  (while paused)
    help = Signal()             #F1
    edit = Signal()             #F2
    togglePlay = Signal()       #F7 <space>
    recordBuffer = Signal()     #F12
    
    # signals (new)
    processFrame = Signal(str, object)
    processGroup = Signal(str, object)
    resized = Signal()
    
    def resizeEvent(self, *args, **kwargs):
        returncode = QtGui.QMainWindow.resizeEvent(self, *args, **kwargs)
        self.resized.emit()
        return returncode
    
    @Slot(str,object)
    def settingChanged(self, name, value):
        if name == "delay":
            self.ui.delay.setText(str(value))
        elif name == "keybinding":
            self._loadBindings(value)
        elif name == "selectedlayout":
            self._loadScreens(self.settings.getSetting("layouts")[value]["screen"])
    
    def _loadScreens(self, screens):
        self._screens = screens
        self._layouts = min(4, len(self._screens))
#         print "Layouts: %s" % self._layouts
#         print "Screens: %s" % self._screens
        for i in range(self._layouts):
            self._renderwidgets[i].setLayout(screens[i])
        
    
    def _loadBindings(self, bindings):
        '''
        Extracts the actual key ids from the string representations of them provided.
        
        @param bindings: dict containing keybindings {'<keyname>': [('<group>', '<function>', <optionargs>,...), ...]} 
        '''
        try:
            
            groups = {'core': None,
                    'processframe': lambda m,c: self.processFrame.emit(m,c),
                    'processgroup': lambda m,c: self.processGroup.emit(m,c),
                    }
            corefuncs = {
                         'quit': lambda a,b: self.close(),
                         'play': lambda a,b: self.togglePlay.emit(),
                         'incdelay': lambda a,b: self.incDelay.emit(),
                         'decdelay': lambda a,b: self.decDelay.emit(),
                         'incframe': lambda a,b: self.incFrame.emit(),
                         'decframe': lambda a,b: self.decFrame.emit(),
                         'fullscreen': lambda a,b: self.toggleFullScreen(),
                         'edit': lambda a,b: self.edit.emit(),
                         'help': lambda a,b: self.help.emit(),
                         }
            
            errors = []
            self._bindings = {}
            for keystr, events in bindings.items():
                for event in events:
                    try:
                        # convert to integer
                        keyint = getattr(QtCore.Qt,"Key_%s"% str(keystr))
                        
                        # get functions to perform tasks
                        func = groups[event[0]]
                        if func is None:
                            func = corefuncs[event[1]]
                        
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
    
    def toggleFullScreen(self):
        '''Toggles between fullscreen and normal mode'''
        if not self.isFullScreen():
            self.showFullScreen()
        else:
            self.showNormal()
    
    def keyPressEvent(self, e):
        '''Perform tasks for various key events'''
        
        if e.key() in self._bindings:
            for binding in self._bindings[e.key()]:
                func, action, config = binding
                func(action, config)
        else:
            print "key: %s" % (e.key(),)
    
    def renderFrameset(self, frameset):
        '''
        Renders the relevent frames from the frameset to screen
        '''
        for i in range(self._layouts):
            self._renderwidgets[i].process(frameset)
    
#     def updateView(self, vid, pixmap):
#         '''Updates a view to display given pixmap'''
#         self.ui.videoFrame.setPixmap(pixmap)
#         self.ui.videoFrame.setScaledContents(True)
    
    def setFrameId(self, frameid):
        self.ui.frameNum.setText(frameid)
        
    def setFrameRate(self, framerate):
        self.ui.frameRate.setText(framerate)

# end class MainWindow
