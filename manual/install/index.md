---
layout: page
title: User guide - SportsReview
rooturl: ../../
keywords: SportsReview, user guide, help
---

[Home](../../) > [Manuals](../) > Installation guide

<!--<div class="toc"><ul>
<li><a href="#roadmap">Roadmap</a><ul>
    <li><a href="#v02">v0.2</a></li>
    <li><a href="#v03">v0.3</a></li>
    <li><a href="#v10">v1.0</a></li>
</ul></li>
<li><a href="#complete-versions">Complete versions</a><ul>
    <li><a href="#v01">v0.1</a></li>
</ul></li>
</ul></div>-->

<div class="title">Installation guide</div>

Thank you for deciding to install SportsReview.  Hopefully you will find it an incredbly useful 
training tool and if not please let us know how it can be improved.

# Requirements

SportsReview is fairly flexible in what it can run on.

* **Operating System**: Currently only tested on Debian Linux but plan to support all 3 major OSs
	* *Linux*: Debian (tested) and Redhat based systems (un-tested) 
	* *Windows Vista+*: presently un-tested but *may* work
	* *MacOS*: presently un-tested but *should* work

# Install

1. See the Dependencies section below if you do not have all of the following already installed
	* python
	* pyqt
	* opencv
2. [Download SportsReview](../../download). We recommend the latest version but older ones are there too.
3. Uncompress the archive file
	* Linux and MacOS: run *tar -xzf <vX.X.tar.gz>*
	* Windows: right-click on the .zip file and select Uncompress/Extract
4. Move the directory/folder it creates to a location of your choice.  e.g. your home/document folder
5. See [User Manual](../user) for details on how to run SportsReview

# Dependencies

SportsReview makes use of a few external software programs that need to be installed before you can 

## Python

All SportsReview tools have been writen in the Python scripting language.  The tools were developed using 
version 2.7 but it is hoped that it will be compatible with version 3.3+ (currently un-tested)

### Debian Linux

Installing python on debian-based linux systems is easy and may already be on there

> apt-get install python2.7

alternatively: (note: not yet tested)

> apt-get install python3.3

### Redhat Linux

Like debian linux except using:

> yum install python

### MacOS

Apparently Mac comes pre-installed with python.  If, however, the version is tool old please see this page 
on how to install a newer version https://www.python.org/download/mac/

### Windows

Python needs to be installed on windows computers.  You can find a version to download on the from the 
following page: https://www.python.org/download/releases/.  It is recommended that you uses a version 
starting with 2.7 (currently 2.7.6) at this point as 3 versions have not been tested with SportsReview yet.

## PyQt or PySide

The Graphical user interface makes use of the Qt cross-platform toolkit.  There are plans to make it support 
both PySide and PyQt however at this point it only supports PyQt

### Debian Linux

> apt-get install python-qt4-dev

Note:I think, it was already installed on my system and yet to test on a blank system

## OpenCV

Currently the only Camera capture modules that have been implemented make use of OpenCV.  We plan to make 
other alternatives as this can be difficult to install on some systems.

### Debian Linux

> apt-get install python-opencv

Alternatively you can install the latest version from the OpenCV website

http://opencv.org/downloads.html

### Redhat Linux

TODO: find/test the packages required

http://opencv.org/downloads.html

### MacOS

Install the latest version from the OpenCV webpage

http://opencv.org/downloads.html

### Windows

Install the latest version from the OpenCV webpage

http://opencv.org/downloads.html

## Git

[Optional] this is used if you are planing to develop and possibly in the future we will use it to auto-update
your version of SportsReview

See http://git-scm.com/book/en/Getting-Started-Installing-Git

