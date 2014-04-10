---
layout: page
title: Roadmap - SportsReview
rooturl: ../
keywords: SportsReview, roadmap, features, upcoming
---

[Home](../) > [Design notes](./) > Roadmap

<div class="toc"><ul>
<li><a href="#roadmap">Roadmap</a><ul>
    <li><a href="#v02">v0.2</a></li>
    <li><a href="#v03">v0.3</a></li>
    <li><a href="#v10">v1.0</a></li>
</ul></li>
<li><a href="#complete-versions">Complete versions</a><ul>
    <li><a href="#v01">v0.1</a></li>
</ul></li>
</ul></div>

# Roadmap
The roadmap details current feature plans for next and following releases of SportsReview. 
	
## v0.2
Probable inclusions for v0.2; some may be moved to v0.3

* Delay analysis tool
	* Add module API [3/4 Done]
	* Move webcam capture to module [Done]
	* Move frame buffer to module [Done]
	* Move write buffer to module [Done]
	* Support multiple capture devices [Done]
	* Screen layout configuration (settings file) [Done]
	* Improved on-screen overlay (implement multiple groups, scaled font size)
* After touches tool: (new)
	* Load saved buffer
	* Replay and various speeds
	* Replay frame-by-frame
	* Clip ends of buffer
	* Split buffer
	* Merge multiple buffers
	* Export to video formats (single cam and multi-layout)

## v0.3
Probable inclusions for v0.3

* Delay analysis tool:
	* add core function to switch layouts (inc, dec and jumpto)
	* AVI (and other) video format exporters
	* size hinting to capture devices (from renderwidget size)
* After touches tool:
	* allow user to resize each renderwidget on layout

## v1.0
Minimum requirements for version 1.0

* Unit-testing on all major components
* User documentation
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
* Delay video tool:
	* Configurable UI layout
* Analysis tool:
	* Track multi-segment lines between frames

### v1.0 maybe's
Some other ideas that may make it into version 1.0

* Support either PySide (default) or PyQt
* Support client/server: allows users to connect to a support server and get help
	* IM chat
	* send files to server (user send or supporter request)

# Complete versions
Versions that have been completed

## v0.1
* Delay video tool:
	* Single webcam capture
	* Delay video buffer
	* Pause stream
	* Write buffer
	* Change various settings with keypresses
	* Add key-bindings in settings file
	* Add write-buffer path in settings file
	* Improved on-screen overlay
