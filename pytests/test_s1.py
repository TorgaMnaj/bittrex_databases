#!/usr/bin/env python3
# Copyright (c) 2020 Jan Magrot

import time


def test_settings_reading():
	import lib.SettingsReader as Sr
	co = Sr.Config()
	pass


def test_logger():
	with open("./logs/app.log", "w") as o:
		o.write("")
	import logging
	import bittrex_database
	mlogger = logging.getLogger("bittrex_database." + __name__)
	mlogger.debug("Test.")
	with open("./logs/app.log", "r") as o:
		s = o.readline()
		s = s.split("\n")[0]
	assert "Test" in s
	assert "bittrex_database." + __name__ in s


def test_api():
	import lib.bittrex_api as Ba
	PublicApi = Ba.PublicApi()
	currencies = PublicApi.getAllCurrenciesInfo()
	time.sleep(1)
	assert isinstance(currencies, dict)
	assert len(currencies) > 200
	getAllMarketsInfo = PublicApi.getAllMarketsInfo()
	time.sleep(1)
	assert isinstance(getAllMarketsInfo, dict)
	assert len(getAllMarketsInfo) > 200
	getAllMarketsSummaries = PublicApi.getAllMarketsSummaries()
	time.sleep(1)
	assert isinstance(getAllMarketsSummaries, dict)
	assert len(getAllMarketsSummaries) > 200
	getAllMarketsTicker = PublicApi.getAllMarketsTicker()
	time.sleep(1)
	assert isinstance(getAllMarketsTicker, dict)
	assert len(getAllMarketsTicker) > 200
	s = PublicApi.pingBittrex()
	assert isinstance(s, dict)
