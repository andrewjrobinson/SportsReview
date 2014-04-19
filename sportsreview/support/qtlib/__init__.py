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
Loads qt libraries in a standard interface
'''

import sys

from pyqtnone import *
from pyqtnone import __implementation__, __version__

## import PySide code ##
_loaded_ = False
_tryingPyQt = False
try:
    from pyside import *
    _loaded_ = True
except ImportError:
    pass

## try failing over to PyQt ##
# uncomment the following to fail over to PyQt #
# if not _loaded_:
#     try:
#         _tryingPyQt = True
#         from pyqt import *
#         _loaded_ = True
#     except ImportError:
#         pass
# end uncomment #

# make sure one succeeded
if not _loaded_:
    if _tryingPyQt:
        sys.stderr.write("Failed to load a Python Qt library (tried PySide and PyQt)\n");
    else:
        sys.stderr.write("Failed to load a Python Qt library (tried PySide only)\n");
        sys.stderr.write("If you have PyQt installed try un-commenting the required section in \n");
        sys.stderr.write("'sportsreview/support/__init__.py'\n");
    raise Exception("Failed to load a Python Qt library")

# print "Loaded %s v%s" % (__implementation__, __version__)
