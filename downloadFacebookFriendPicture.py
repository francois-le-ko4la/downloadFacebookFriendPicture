#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This script is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This script is provided in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from RestAPIController import RestAPIController
from smoothProgressBar import smoothProgressBar
from configParser import configParser

import sys
import os
import json
import urllib
from urllib.parse import urlencode, quote_plus

myConfigParser=configParser('facebook.json')
sessionParameter=myConfigParser.get()
myFBRestAPI=RestAPIController(
                        token=sessionParameter['data']['token'],
                        host=sessionParameter['data']['host'],
                        DEBUG=sessionParameter['debug']
                        )
myFBRestAPI.request("GET", "/v2.12/me/taggable_friends", {'fields':'id,name,picture.width(500).height(500).type(large)','limit':'5000'})

friendsList = myFBRestAPI.get()
myPB=smoothProgressBar()
myPB.start(len(friendsList['data']))

i=0
for friend in friendsList['data']:
    try:
        myPB.update(i, friend['name']+" - Saving picture...")
        pictureURL = str(friend['picture']['data']['url'])
        picture = urllib.request.urlopen(pictureURL).read()
        f = open("./pictures/"+friend['name'] + '.jpg', 'wb')
        f.write(picture)
        f.close()
        i+=1
        myPB.update(i, friend['name']+" - Saved...")
    except:
        print("Can't save "+friend['name']+" Saved !")
myPB.stop()

