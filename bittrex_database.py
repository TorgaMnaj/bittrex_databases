#!/usr/bin/env python3
# Copyright (c) 2021 Jan Magrot

import logging

logger = None


def Logger():
	# Logger:
	global logger
	logger = logging.getLogger('bittrex_database')
	logger.setLevel(logging.DEBUG)
	fh = logging.FileHandler('./logs/app.log')
	fh.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	logger.addHandler(fh)


Logger()
