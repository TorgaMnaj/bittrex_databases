#! /usr/bin/make -f
VENV        := $(CURDIR)/venv
PYTHON_BIN  ?= $(VENV)/bin/python3
PIP_BIN     ?= $(VENV)/bin/pip
APP			?= ./*.py

help:  		## This help dialog.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

devinstall:	## Install development tools
	cat dev_requirements.apt | xargs sudo apt install -y

bootstrap:  	## Bootstrap project or fix existing copy
	sudo apt update
	cat requirements.apt | xargs sudo apt install -y
	pip3 install -r requirements.txt

run:  		## Start development version of application
	python3 $(APP)

bashtests:  	## Run bash scripts tests
	bash ./.devbin/shtests.sh

pyttests:  	## Run applications python tests
	chmod -R 755 ./*
	$(PYTHON_BIN) -m pytest pytests/
	bash ./.devbin/pylint.sh

commit:  	## Deploy, test, commit changes to git and push on github
	bash ./.devbin/bigcommit.sh
