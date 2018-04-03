#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# downloadFacebookFriendPicture
## Description:

The following files comprise the `downloadFacebookFriendPicture` package:
* `LICENSE`: The license file. `downloadFacebookFriendPicture` is released
under the terms of the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `download_fbfriendpicture.py`: The code of interest.
* `facebook.json.sample`: Sample config file

## Setup:
```shell
    git clone https://github.com/francois-le-ko4la/downloadFacebookFriendPicture.git
    cd downloadFacebookFriendPicture
    make install
```

## How to use this script:

* Create a facebook APP
* change JSON file
```shell
cp facebook.json.sample facebook.json
vi facebook.json
```

* launch the script
```
./download_fbfriendpicture.py
```

## Note:

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Todo:

    - [X] Create the project
    - [X] Write code and tests
    - [X] Test installation and requirements (setup.py and/or Makefile)
    - [X] Test code
    - [X] Validate features
    - [X] Write Doc/stringdoc
    - [X] Run PEP8 validation
    - [ ] Clean & last check
    - [ ] Release

"""

import urllib
from rest_api_controller import RestAPIController
from smooth_progressbar import SmoothProgressBar
from config_from_json import ConfigFromJSON


def download_fbfriendpicture():
    """Download pictures
    """

    my_config = ConfigFromJSON('facebook.json')

    if my_config.read() is not True:
        print("JSON Error")
        exit(1)

    my_params = my_config.get()

    my_fb_api = RestAPIController(
        token=my_params['data']['token'],
        host=my_params['data']['host'],
        DEBUG=my_params['debug']
        )
    # test if we can reach the server
    if my_fb_api.isconnected() is not True:
        print("Server unreachable...")
        exit(1)
    else:
        print("Server: OK")

    my_fb_api.request(
        "GET",
        "/v2.12/me/taggable_friends",
        {
            'fields': 'id,name,picture.width(900).height(900).type(large)',
            'limit': '5000'}
        )

    # get the request status
    if my_fb_api.isrequested() is not True:
        print("Request errot...")
        exit(1)
    else:
        print("Request: OK")

    friends = my_fb_api.get()
    my_progressbar = SmoothProgressBar()
    my_progressbar.start(len(friends['data']))

    i = 0
    for friend in friends['data']:
        try:
            my_progressbar.update(i, friend['name']+" - Saving picture...")
            picture_url = str(friend['picture']['data']['url'])
            picture = urllib.request.urlopen(picture_url).read()
            file_to_save = open("./pictures/"+friend['name'] + '.jpg', 'wb')
            file_to_save.write(picture)
            file_to_save.close()
            i += 1
            my_progressbar.update(i, friend['name']+" - Saved...")
        except ValueError:
            print("Can't save "+friend['name']+" Saved !")
    my_progressbar.stop()

if __name__ == '__main__':
    download_fbfriendpicture()
