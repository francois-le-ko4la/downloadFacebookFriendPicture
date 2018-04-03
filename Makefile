# Makefile

PACKAGE_NAME = downloadFacebookFriendPicture
MAKE := $(MAKE) --no-print-directory
SHELL = bash

default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make install    install the packages' 
	@echo '    make clean      remove the package'
	@echo

install:
	@sudo ./setup.sh

clean:
	@sudo -H pip3 uninstall -y config-from-json
	@sudo -H pip3 uninstall -y rest-api-controller
	@sudo -H pip3 uninstall -y smooth-progressbar

publish:
	@git add .
	@git commit
	@git push

test:
	@echo 'Pep 8 - in progress...'
	@pep8 download_fbfriendpicture.py
	@echo 'Pep 8 - OK !'

.PHONY: default install clean
