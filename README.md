# downloadFacebookFriendPicture
## Description:

Download Friends' picture from facebook API.

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
```shell
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
- [ ] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [ ] Clean & last check
- [ ] Release

