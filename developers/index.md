---
layout: page
title: Developer notes - SportsReview
rooturl: ../
keywords: SportsReview, developers, development
---

[Home](../index.html) > Design notes

#Design notes

Some notes for developers.

See [Roadmap](roadmap.html) for details about when a given feature is planned

##Tools overview

SportsReview is made up of a number of tools that specialise on certain tasks.  Each tool is extendable 
using a common module API. 

###Delay analysis

Allows user to capture live streams of video and/or other numerical from various captuer devices such
as accelerometers etc.

* Live play: i.e. view action with a configurable delay
* Pause: pause live play and view frame-by-frame
* Record: save a buffer of frames to disk for later analysis


###After touches
Allows the user to open captures made during delay analysis and perform various tasks with them:

* Export video: in various formats and help put these files onto an external storage device.
	* Ultimately this would allow merging of multiple capture devices and include any analysis overlays
* Analyse: run an analysis module over a frame or framegroup.  These could perform tasks:
	* render bat position on video image
	* locate features from video frame (i.e. person and joints)

##Modular
The core code will be kept to a minimum and use modules to extend the features of the software.  
Three directories will exist to contain modules; 2 in the installation directory and an optional 
(admin disableable) user override directory (in each users home/settings).

Modules can implement one or more of the following interfaces:
* CaptureFrame: capture details from a hardware device such as video cam, on-bat accelerometers
* ProcessFrame: process a single frame and optionally produce an overlay or text output
* CaptureGroup: capture a group of details from a filesource or capture on video device
* ProcessGroup: process a group of frames

##OS independent
All attempts will be made to allow the code to run on Linux, Windows and Mac OS

##Package friendly
Source and settings configurable to make it easy for package maintainers to package the software.  
env.py will specify the source files/dirs that contain settings files.  It will also allow the 
maintainer to disable the software update feature (though it will allow the user to install a 
local copy that can be updated)

##Software updates
Use git to manage files.  A local git repo (called working repo) within program is used to download 
new versions of program files (python files).  The git repo can be configured to use the github repo 
or a clone of it that is on a mounted filesystem (e.g. usbdisk) for computers that are not internet 
connected.

A GUI and CLI client will allow the user to update the working repo from a configured remote, view 
the versions that are available (tags) and install a particular version (or a dev version by its hashid)
during install the system will backup the current installation (and keep a number of versions).

##Implementation

###Dependencies
* Python 2.x or 3.x [Only tested on 2.7]
* PyQt or PySide: [PySide not yet supported]
* pyCV: (OpenCV)
* git: for software updates [not yet]

###Development Repository
A public (open source) repo hosted on github will be used for version control and also for software 
distribution.

Branches:
* master: for stable releases
* dev: for active development
* testing: for pre-release testing

###Source/runtime tree
* aftertouches: package for application code of the after touches tool [TODO: implement this]
	* ui: package for ui files
	* main.py: the execution entry point
* common: package for code that is shared among tools
* delayvideo: package for application code of the delay analysis tool
	* ui: package for ui files
	* main.py: the execution entry point
* modules: package for modules that are included within sportsreview
	* \_\_init\_\_.py: currently imports all modules, later this will be done away with.
	* \*.py: one file for each sportsreview module, name all lowercase
* settings: package for settings related modules
	* settingsmanager.py: central place for loading and saving settings files
	* \*.py: the settings files for various configurations.  settings.py is the default.
* support: package for system specific code. i.e. duplicate implementations of functions for each version of python etc.
	* \_\_init\_\_.py: imports the correct system specific code.  i.e. 'import support' to load the correct version of the functions for your system
	* versionX.py: implementations for version X of python.
	* osY.py: implementations for operating system Y.  e.g. oslinux.py, oswin.py etc.
* test: package full of random code used for R&D.  
	* TODO: remove this and replace with unittests
* env.py: global overrides for settings and disabling software updates

###APIs
The modules can have a number of different functions, this section describes that a module must implement to
perform each of these functions

####All modules
* getModule(cls, settings, config): a class level function used to create an instance of the module
	* param: settings, the global settings object
	* param: config, module specific configuration (per instance)
	* return: the Module instance
* A set of class level constants describing the API's this module implements, set True each supported api
	* \_\_CAPTURE_FRAME\_\_ = False
	* \_\_PROCESS_FRAME\_\_ = False
	* \_\_CAPTURE_GROUP\_\_ = False
	* \_\_PROCESS_GROUP\_\_ = False

####CaptureFrame
* 


