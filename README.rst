=============================
downloadFacebookFriendPicture
=============================

Warning
=======

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Description
===========

The following files comprise the downloadFacebookFriendPicture package:

* LICENSE: The license file. configParser is released under the terms of the GNU General Public License (GPL), version 3.
* README.rst: This readme file.
* Makefile: The setup file. See above for installation instructions.

Setup
=====

>>> git clone https://github.com/francois-le-ko4la/downloadFacebookFriendPicture.git
>>> cd downloadFacebookFriendPicture
>>> make install

How to use this script
======================

* Create a facebook APP
* change JSON file

>>> cp facebook.json.sample facebook.json
>>> vi facebook.json

* launch the script

>>> ./download_fbfriendpicture.py
