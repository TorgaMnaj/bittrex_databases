#!/usr/bin/env python3
# Copyright (c) 2021 Jan Magrot

import logging
import lib.Bittrex_api as Ba
import lib.Databases as Db

logger = None


def Logger():
	# clean
	with open("./logs/app.log", "w") as o:
		o.write("")
	# Logger:
	global logger
	logger = logging.getLogger('bittrex_database')
	logger.setLevel(logging.INFO)
	fh = logging.FileHandler('./logs/app.log')
	fh.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	logger.addHandler(fh)


Logger()


def BuildTables():
	Db.removeAllDatabases()
	pa = Ba.PublicApi()
	currinfo = pa.getAllCurrenciesInfo()
	marketsinfo = pa.getAllMarketsInfo()
	currencies = {k for k in currinfo.keys()}
	markets = {k for k in marketsinfo.keys()}
	Db.createAllDatabases(currencies, markets)
	#
	for k, v in currinfo.items():
		Db.insertCurrenciesInfo(k, v)
	for k, v in marketsinfo.items():
		Db.insertMarketsInfo(k, v)


BuildTables()
