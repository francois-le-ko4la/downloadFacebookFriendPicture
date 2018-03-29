# Makefile

PACKAGE_NAME = humanfriendly
MAKE := $(MAKE) --no-print-directory
SHELL = bash

default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make install    install the packages' 
	@echo

install:
	@pip3 install git+https://github.com/francois-le-ko4la/configParser.git
	@pip3 install git+https://github.com/francois-le-ko4la/RestAPIController.git
	@pip3 install git+https://github.com/francois-le-ko4la/smoothProgressBar.git

clean:
	@rm -Rf *.egg .cache .coverage .tox build dist docs/build htmlcov
	@find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@find -type f -name '*.pyc' -delete

.PHONY: default install test publish clean
