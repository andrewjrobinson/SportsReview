---
layout: page
title: Roadmap - SportsReview
rooturl: ../
keywords: SportsReview, roadmap, features, upcoming
---

[Home](../) > [Design notes](./) > Roadmap

<div class="toc"><ul>
<li><a href="#roadmap">Roadmap</a><ul>
    <li><a href="#v03">v0.3</a></li>
    <li><a href="#v10">v1.0</a></li>
</ul></li>
<li><a href="#complete-versions">Complete versions</a><ul>
    <li><a href="#v02">v0.2</a></li>
    <li><a href="#v01">v0.1</a></li>
</ul></li>
</ul></div>

<div class="title" id="roadmap">Roadmap</div>

The roadmap details current feature plans for next and following releases of SportsReview. 

# v0.3
Probable inclusions for v0.3; some may be moved to v0.4

* Delay analysis tool:
	* add core function to switch layouts (inc, dec and jumpto)
	* AVI (and other) video format exporters
	* size hinting to capture devices (from renderwidget size)
	* Improved on-screen overlay (scaled font size)
* After touches tool:
	* Add support for 'project'
		* file format
		* import multiple frame groups
	* Split framegroup
	* Interupt playback (pause, change speed)
	* Merge multiple framegroups
	* Stream-merge module i.e. combine multiple cams (or other devices) into a single image (ready for export)
	* Save changes (i.e. clipping etc.)

# v1.0
Minimum requirements for version 1.0

* Unit-testing on all major components
* User documentation
	* Installation Guides (including dependencies)
	* Tool usage guides
	* Typical hardware/software setup guides
* Developer documentation
	* Details of each function of the module API
	* Example module implementations for each major type
* Multiple OS support (Windows, Mac, Linux)
* Setting editor: A gui that allows editing of all settings (openable from within all tools)
* Software update manager
	* Check for updates
	* Perform update (selectable version; any stable versions, any dev commit)
* Delay analysis tool:
	* Configurable UI layout
* After touches tool:
	* Configurable UI layout
	* Track multi-segment lines between frames

## v1.0 maybe's
Some other ideas that may make it into version 1.0

* Support client/server: allows users to connect to a support server and get help
	* IM chat
	* send files to server (user send or supporter request)

<div class="title" id="complete-versions">Complete versions</div>

Versions that have been completed
	
# v0.2
* Common:
	* Add module API
	* Support either PySide (default) or PyQt (disabled)
* Delay analysis tool
	* Move webcam capture to module
	* Move frame buffer to module
	* Move write buffer to module
	* Support multiple capture devices
	* Screen layout configuration (settings file)
	* Improved on-screen overlay (implement multiple groups)
* After touches tool: (new)
	* Load saved buffer
	* Replay and various speeds/directions
	* Replay frame-by-frame
	* Clip ends of framegroup (run-time only)
	* Export framegroup to video formats (single cam)

# v0.1
* Delay video tool:
	* Single webcam capture
	* Delay video buffer
	* Pause stream
	* Write buffer
	* Change various settings with keypresses
	* Add key-bindings in settings file
	* Add write-buffer path in settings file
	* Improved on-screen overlay
