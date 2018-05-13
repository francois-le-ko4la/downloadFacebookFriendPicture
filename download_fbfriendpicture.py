#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# downloadFacebookFriendPicture - code breaking

This package used Facebook API to download friends' picture.
Due to policy change, it can't be used anymore.

https://developers.facebook.com/docs/graph-api/changelog/breaking-changes/
```
4/4/2018
...
Returns Empty Set — The following nodes and edges will now only return empty data sets:

    /achievement_id
    /app/achievements
    /app/scores
    /user/achievements
    /user/invitable_friends
    /user/scores
    /user/taggable_friends
```

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
        debug=True
        #my_params['debug']
        )

    friends = my_fb_api.request(
        "GET",
        "/v2.12/me/taggable_friends",
        {
            'fields': 'id,name,picture.width(900).height(900).type(large)',
            'limit': '5000'}
        )


    print(friends)
    exit(1)
    if friends is None:
        print("Error")
        exit(1)

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
