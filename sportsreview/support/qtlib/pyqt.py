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
Standardisation of PyQt symbols.  Note this file uses PyQt which is licenced under
GPL.  Using it will render the whole application GPL (rather than LGPL).  By default
this module is not used, and only provided for users who have PyQt installed and
don't want to use PySide.

@see: __init__.py: for details on loading this module.

Created on 19/04/2014
@author: Andrew Robinson
'''

__all__ = ['QtCore', 'QtGui', 'Slot', 'Signal', '__implementation__', '__version__']

import PyQt4.Qt
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot as Slot
from PyQt4.QtCore import pyqtSignal as Signal

__implementation__ = 'PyQt'
__version__ = PyQt4.Qt.PYQT_VERSION_STR
