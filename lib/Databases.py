#!/usr/bin/env python3
# Copyright (c) 2021 janmagrot@gmail.com

import pymysql
import logging

module_logging = logging.getLogger("bittrex_database." + __name__)


def parse_sql_file(filename, variable=None, replacement=None):
	"""
	conn = pymysql.connect('test')
	stmts = parse_sql('my_sql_file.sql')
	with conn.cursor() as cursor:
        for stmt in stmts:
            cursor.execute(stmt)
    conn.commit()
	:param replacement:
	:param variable:
	:param filename:
	:return:
	"""
	data = open(filename, 'r').readlines()
	stmts = []
	DELIMITER = ';'
	stmt = ''

	for lineno, line in enumerate(data):
		if variable and replacement:
			if variable in line:
				line.replace(variable, replacement)

		if not line.strip():
			continue

		if line.startswith('--'):
			continue

		if 'DELIMITER' in line:
			DELIMITER = line.split()[1]
			continue

		if DELIMITER not in line:
			stmt += line.replace(DELIMITER, ';')
			continue

		if stmt:
			stmt += line
			stmts.append(stmt.strip())
			stmt = ''
		else:
			stmts.append(line.strip())
	return stmts


def createDatabases():
	"""
	Function for creating databases.
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982')
	func_logging = logging.getLogger("bittrex_database." + str(__name__) + ".createDatabases()")
	stmts = parse_sql_file("./databases/create_databases.sql")
	with conn.cursor() as cursor:
		for stmt in stmts:
			cursor.execute(stmt)
	conn.commit()
	func_logging.info("Initial empty databases without columns, have been created.")
	return True


def createCurrenciesInfoDatabases(currencies, database):
	"""
	Function that creates tables for informations about
	currencies.
	:param database:
	:param currencies:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database=database)
	func_logging = logging.getLogger("bittrex_database." + str(__name__) + ".createCurrenciesInfoDatabases()")
	for ix in currencies:
		with conn.cursor() as cur:
			comm = f'CREATE OR REPLACE TABLE `{ix}` (' \
			       f'symbol CHAR(12) NOT NULL, ' \
			       f'name CHAR(20) NOT NULL, ' \
			       f'status CHAR(10) NOT NULL,' \
			       f'minConfirmations TINYINT NOT NULL ,' \
			       f'txFee DOUBLE,' \
			       f'baseAddress CHAR(180),' \
			       f'PRIMARY KEY (symbol)' \
			       f') ENGINE=Maria'
			cur.execute(comm)
	conn.commit()
	func_logging.info("Currencies info database have been initiated with empty columns.")
	return True


def createMarketsInfoDatabases(markets, database):
	"""
	Function that creates tables for informations about
	markets.
	:param database:
	:param markets:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database=database)
	func_logging = logging.getLogger("bittrex_database." + str(__name__) + ".createMarketsInfoDatabases()")
	for ix in markets:
		ix = "_".join(str(ix).split("-"))
		with conn.cursor() as cur:
			comm = f'CREATE OR REPLACE TABLE `{ix}` (' \
			       f'symbol CHAR(20) NOT NULL, ' \
			       f'baseCurrencySymbol CHAR(12) NOT NULL, ' \
			       f'quoteCurrencySymbol CHAR(12) NOT NULL, ' \
			       f'minTradeSize FLOAT NOT NULL, ' \
			       f'pprecision TINYINT NOT NULL, ' \
			       f'status CHAR(10) NOT NULL, ' \
			       f'PRIMARY KEY (symbol)' \
			       f') ENGINE=Maria'
			cur.execute(comm)
	conn.commit()
	func_logging.info("Markets info database have been initiated with empty columns.")
	return True


def createOneMinuteCandles(markets, database):
	"""
	Function that creates tables for one minute candles.
	:param database:
	:param markets:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database=database)
	func_logging = logging.getLogger("bittrex_database." + str(__name__) + ".createOneMinuteCandles()")
	for ix in markets:
		with conn.cursor() as cur:
			comm = f'CREATE OR REPLACE TABLE `{ix}` (' \
			       f'symbol CHAR(20) NOT NULL, ' \
			       f'ttime FLOAT NOT NULL, ' \
			       f'oopen DOUBLE NOT NULL, ' \
			       f'hhigh DOUBLE NOT NULL, ' \
			       f'llow DOUBLE NOT NULL, ' \
			       f'cclose DOUBLE NOT NULL, ' \
			       f'base_vol DOUBLE NOT NULL, ' \
			       f'quote_vol DOUBLE NOT NULL, ' \
			       f'usd_vol DOUBLE NOT NULL, ' \
			       f'PRIMARY KEY (symbol, ttime)' \
			       f') ENGINE=Maria'
			cur.execute(comm)
	conn.commit()
	func_logging.info("One minute candles database have been initiated with empty columns.")
	return True


def createFiveMinuteCandles(markets, database):
	"""
	Function that creates tables for five minute candles.
	:param database:
	:param markets:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database=database)
	func_logging = logging.getLogger("bittrex_database." + str(__name__) + ".createFiveMinuteCandles()")
	for ix in markets:
		with conn.cursor() as cur:
			comm = f'CREATE OR REPLACE TABLE `{ix}` (' \
			       f'symbol CHAR(20) NOT NULL, ' \
			       f'ttime FLOAT NOT NULL, ' \
			       f'oopen DOUBLE NOT NULL, ' \
			       f'hhigh DOUBLE NOT NULL, ' \
			       f'llow DOUBLE NOT NULL, ' \
			       f'cclose DOUBLE NOT NULL, ' \
			       f'base_vol DOUBLE NOT NULL, ' \
			       f'quote_vol DOUBLE NOT NULL, ' \
			       f'usd_vol DOUBLE NOT NULL, ' \
			       f'PRIMARY KEY (symbol, ttime)' \
			       f') ENGINE=Maria'
			cur.execute(comm)
	conn.commit()
	func_logging.info("Five minutes candles database have been initiated with empty columns.")
	return True


def createOneHourCandles(markets, database):
	"""
	Function that creates tables for one minute candles.
	:param database:
	:param markets:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database=database)
	func_logging = logging.getLogger("bittrex_database." + str(__name__) + ".createOneHourCandles()")
	for ix in markets:
		with conn.cursor() as cur:
			comm = f'CREATE OR REPLACE TABLE `{ix}` (' \
			       f'symbol CHAR(20) NOT NULL, ' \
			       f'ttime FLOAT NOT NULL, ' \
			       f'oopen DOUBLE NOT NULL, ' \
			       f'hhigh DOUBLE NOT NULL, ' \
			       f'llow DOUBLE NOT NULL, ' \
			       f'cclose DOUBLE NOT NULL, ' \
			       f'base_vol DOUBLE NOT NULL, ' \
			       f'quote_vol DOUBLE NOT NULL, ' \
			       f'usd_vol DOUBLE NOT NULL, ' \
			       f'PRIMARY KEY (symbol, ttime)' \
			       f') ENGINE=Maria'
			cur.execute(comm)
	conn.commit()
	func_logging.info("One hour candles database have been initiated with empty columns.")
	return True


def createAllDatabases(currencies, markets):
	"""
	Function for creating all the databases.
	:return:
	"""
	createDatabases()
	createCurrenciesInfoDatabases(currencies, "currenciesinfo")
	createMarketsInfoDatabases(markets, "marketinfo")
	createOneMinuteCandles(markets, "oneminutecandles")
	createFiveMinuteCandles(markets, "fiveminutescandles")
	createOneHourCandles(markets, "onehourcandles")
	module_logging.info("All databases have been created.")
	return True


def removeAllDatabases():
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982')
	func_logging = logging.getLogger("bittrex_database." + str(__name__) + ".removeAllDatabases()")
	stmts = parse_sql_file("./databases/delete_databases.sql")
	with conn.cursor() as cursor:
		for stmt in stmts:
			cursor.execute(stmt)
	conn.commit()
	func_logging.info("All created databases have been deleted.")
	return True


def insertCurrenciesInfo(currency, currinfo):
	"""
	Inserts informations about currencies
	to table.
	:return:
	"""
	func_logging = logging.getLogger("bittrex_database." + str(__name__) + ".insertCurrenciesInfo()")
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database="currenciesinfo")
	symbol = str(currinfo["symbol"])
	name = str(currinfo["name"])
	status = str(currinfo["status"])
	if "minConfirmations" in currinfo.keys():
		minConfirmations = int(currinfo["minConfirmations"])
	else:
		minConfirmations = ""
	if "txFee" in currinfo.keys():
		txFee = float(currinfo["txFee"])
	else:
		txFee = ""
	if "baseAddress" in currinfo.keys():
		baseAddress = str(currinfo["baseAddress"])
	else:
		baseAddress = ""
	try:
		with conn.cursor() as curr:
			comm = f"INSERT IGNORE INTO {currency}(symbol, name, status, minConfirmations, " \
			       f"txFee, baseAddress) VALUES('{symbol}','{name}','{status}',{minConfirmations}," \
			       f"{txFee},'{baseAddress}');"
			curr.execute(comm)
		conn.commit()
	except Exception:
		func_logging.exception("Exception during inserting currencies informations.")
	func_logging.debug("Databases about currencies info have been filled with data.")
	return True


def insertMarketsInfo(market, marketinfo):
	"""
	Inserts informations about currencies
	to table.
	:return:
	"""
	func_logging = logging.getLogger("bittrex_database." + str(__name__) + ".insertMarketsInfo()")
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database="marketinfo")
	market = "_".join(str(market).split("-"))
	symbol = "_".join(str(marketinfo["symbol"]).split("-"))
	baseCurrencySymbol = str(marketinfo["baseCurrencySymbol"])
	quoteCurrencySymbol = str(marketinfo["quoteCurrencySymbol"])
	minTradeSize = float(marketinfo["minTradeSize"])
	pprecision = int(marketinfo["precision"])
	status = str(marketinfo["status"])
	try:
		with conn.cursor() as curr:
			comm = f"INSERT IGNORE INTO {market}(symbol, baseCurrencySymbol, quoteCurrencySymbol, minTradeSize, " \
			       f"pprecision, status) VALUES('{symbol}','{baseCurrencySymbol}','{quoteCurrencySymbol}',{minTradeSize}," \
			       f"{pprecision},'{status}');"
			curr.execute(comm)
		conn.commit()
	except Exception:
		func_logging.exception("Exception during inserting markets informations.")
	func_logging.debug("Databases about markets info have been filled with data.")
	return True
