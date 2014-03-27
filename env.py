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
Created on 27/03/2014

@author: arobinson
'''

'''Allow users to have settings files in their home dir'''
USER_SETTINGS = False

'''Allow users to have modules in their home dir'''
USER_MODULES = False

'''
Override the global default settings file (package manager defaults)

Default: /etc/sportsreview/defaults.py (Linux/Mac)
         C:\Program Files\Sports Review\defaults.py (Windows)
         $SPORTSREVIEWROOT/defaults.py (user-install)
'''
GLOBAL_DEFAULT_SETTINGS = None

'''
Override the global settings directory (admin changes)

Default: /etc/sportsreview/conf.d/ (Linux/Mac)
         C:\Program Files\Sports Review\settings\ (Windows)
         $SPORTSREVIEWROOT/settings/ (user-install)
'''
GLOBAL_SETTINGS = None

