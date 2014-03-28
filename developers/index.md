---
layout: post
title: Blogging Like a Hacker
---
#Tools
##Delay analysis

##After touches
Allows the user to open captures made during delay analysis and perform various tasks with them:
* Export video: in various formats and help put these files onto an external storage device.
 * Ultimately this would allow merging of multiple capture devices and include any analysis overlays
* Analyse: run an analysis module over a frame or framegroup.  These could perform tasks:
 * render bat position on video image
 * locate features from video frame (i.e. person and joints)

It allows the run
#Modular
The core code will be kept to a minimum and use modules to extend the features of the software.  Three directories will exist to contain modules; 2 in the installation directory and an optional (admin disableable) user override directory (in each users home/settings).

Modules can implement one or more of the following interfaces:
* Frame: process a single frame and optionally produce an overlay or text output
* IO: capture details from a hardware device such as video cam, on-bat accelerometers
* FrameGroup: process a group of frames (may not need this one)
#OS independent
All attempts will be made to allow the code to run on Linux, Windows and Mac OSs
#Package friendly
Source and settings configurable to make it easy for package maintainers to package the software.  env.py will specify the source files/dirs that contain settings files.  It will also allow the maintainer to disable the software update feature (though it will allow the user to install a local copy that can be updated)
#Software updates
Use git to manage files.  A local git repo (called working repo) within program is used to download new versions of program files (python files).  The git repo can be configured to use the github repo or a clone of it that is on a mounted filesystem (e.g. usbdisk) for computers that are not internet connected.
A GUI and CLI client will allow the user to update the working repo from a configured remote, view the versions that are available (tags) and install a particular version (or a dev version by its hashid)
during install the system will backup the current installation (and keep a number of versions).
#Implementation
##Dependencies
* Python 2.x or 3.x
* PyQt or PySide:
* pyCV: (OpenCV)
* git: for software updates
##Development Repository
A public (open source) repo hosted on github will be used for version control and also for software distribution.  
Branches:
* master: for stable releases
* dev: for active development
* testing: for pre-release testing
##Source/runtime tree
* settings: a directory that contains global settings files
* env.py: global overrides for settings and disabling software updates
