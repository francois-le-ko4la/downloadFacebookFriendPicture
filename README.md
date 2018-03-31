# downloadFacebookFriendPicture
## Description:

Download Friends' picture from facebook API.

The following files comprise the downloadFacebookFriendPicture package:
* LICENSE: The license file. configParser is released under the terms of
the GNU General Public License (GPL), version 3.
* README.rst: This readme file.
* Makefile: The setup file. See above for installation instructions.

## Setup:

    git clone https://github.com/francois-le-ko4la/downloadFacebookFriendPicture.git
    cd downloadFacebookFriendPicture
    make install

## How to use this script:

* Create a facebook APP
* change JSON file
```
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

## Dev docstring
### Class ConfigFromJSON:
This Class provides a dict from a JSON File.
You can use it to avoid a lot of CONST in your scripts.

#### Function ConfigFromJSON.__init__(self, json_file):

```
Init the ConfigFromJson Class
This function define self.config and self.__json_file
By default:
    self.config = None

Args:
    json_file (str): /path/to/the/json/file

Attributes:
    __json_file (str): /path/to/the/json/file
    self.config (dict): This value will be updated by reading
    the JSON File

Returns:
    obj
```

#### Function ConfigFromJSON.get(self):

```
Provides the config

Args:
    None

Returns:
    Dict
```

#### Function ConfigFromJSON.get_item(self, key):

```
Select an Item with a key

```

#### Function ConfigFromJSON.read(self):

```
Read a JSON file & set self.config

Args:
    None

Returns:
    True if successful, False otherwise.
```

### Class RestAPIController:
My REST API Controller


#### Function RestAPIController.__enable_debug(self):

```
Enable Debug
-> connection log

Args:
    None

Returns:
    None
```

#### Function RestAPIController.__init__(self, *args, **kwargs):

```
Init the RestAPIController Class
This function define attributes.

Args:
    *arg/**kwargs
        auth(dict)
        token(dict)
        host(string)
        DEBUG(bool)

Attributes:
    self.__connected(bool)
    self.__requested(bool)
    self.__auth(dict)
    self.__token(dict)
    self.__debug(bool)
    self.__host(string)
    self.__result(dict)

Returns:
    obj
```

#### Function RestAPIController.get(self):

```
Get All values

Args:
    None

Returns:
    self.__result(dict): REST API response
```

#### Function RestAPIController.get_connect_status(self):

```
Get connection status

Args:
    None

Returns:
    self.__connected(bool)
```

#### Function RestAPIController.get_item(self, item_key, item_id):

```
Get one value

```

#### Function RestAPIController.get_request_status(self):

```
Get request status

Args:
    None

Returns:
    self.__requested
```

#### Function RestAPIController.request(self, method=None, path=None, args=None):

```
API Request

Args:
    method(str): "GET", "PUT" ...
    path(str): url = host+path
    args(dict): HTTP args

Returns:
    True if successful, False otherwise.
```

### Class SmoothProgressBar:
This Class provides a progressbar

#### Function SmoothProgressBar.__get_bar(self):

```
This function provides the string to print the progress and
informations

Call __get_percentbar(), self.__get_infosbar and provides a complete
progress bar

Args:
    None

Returns:
    string: Processing (70.0%): |///////////////     | 0:00:01 | task 1
```

#### Function SmoothProgressBar.__get_elapse(self):

```
This function provides elapse time between start() and now.

self.__update_time-self.__start_time

Args:
    None

Returns:
    datetime object
```

#### Function SmoothProgressBar.__get_infosbar(self):

```
This function provides an information to print.

Provides : Elapse and description.

Args:
    None

Returns:
    string: "{elapse} | {description}"
```

#### Function SmoothProgressBar.__get_percentbar(self):

```
This function provides the string to print the progress

Provides progress and bar according to the screen size.

Args:
    None

Returns:
    string: Processing (70.0%): |///////////////     |
```

#### Function SmoothProgressBar.__refresh(self):

```
This function refresh the progress bar

Call __get_bar(), print the string, call Timer functions to recall

Args:
    None

Returns:
    None
```

#### Function SmoothProgressBar.__set_percent(self):

```
This function provides current percent.

current_percent=round(self.__current_value/float(self.__max_value), 1)

Args:
    None

Returns:
    None
```

#### Function SmoothProgressBar.__init__(self):

```
Init the smoothProgressBar Class
This function define attributes.

Args:
    None

Attributes:
    self.__interval(float) : refresh time
    self.__rows(float): screen size
    self.__columns(float): screen size
    self.__text(str): text to print
    self.__bar_length(int): progressbar size
    self.__start_time(datetime): start time
    self.__update_time(datetime): update time
    self.__max_value(int): maximum value (100%)
    self.__description(str):
    self.__current_value(int):
    self.__current_percent(float)
    self.__is_running(bool)
    self.__is_updated(bool)
    self.__previous_percent(str)

Returns:
    obj
```

#### Function SmoothProgressBar.start(self, max_value):

```
This function start the progress bar

Test if the progress is already running, set _startTime,
call Timer functions to refresh

Args:
    max_value(int): the value at 100%.

Returns:
    None
```

#### Function SmoothProgressBar.stop(self):

```
This function stop the progress bar.

Args:
    None

Results:
    None
```

#### Function SmoothProgressBar.update(self, current_value, description=None):

```
This function update currentValue, description, __update_time
and call __set_percent().

Args:
    current_value(int): current value
    description(string): current description

Returns:
    None
```

### Function download_fbfriendpicture():

```
Download pictures

```

