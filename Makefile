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
	@pip3 install git+https://github.com/francois-le-ko4la/config-from-json.git
	@pip3 install git+https://github.com/francois-le-ko4la/rest-api-controller.git
	@pip3 install git+https://github.com/francois-le-ko4la/smooth-progressbar.git

clean:
	@rm -Rf *.egg .cache .coverage .tox build dist docs/build htmlcov
	@find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@find -type f -name '*.pyc' -delete
	@pip3 uninstall -y config-from-json
	@pip3 uninstall -y rest-api-controller
	@pip3 uninstall -y smooth-progressbar

.PHONY: default install clean
