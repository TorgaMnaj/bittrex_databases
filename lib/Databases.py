#!/usr/bin/env python3
# Copyright (c) 2021 janmagrot@gmail.com

import pymysql


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
	Function for creating tables.
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982')
	stmts = parse_sql_file("./databases/create_databases.sql")
	with conn.cursor() as cursor:
		for stmt in stmts:
			cursor.execute(stmt)
	conn.commit()


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
	for ix in currencies:
		with conn.cursor() as cur:
			comm = f'CREATE OR REPLACE TABLE `{ix}` (' \
			       f'symbol CHAR(12) NOT NULL, ' \
			       f'name CHAR(20) NOT NULL, ' \
			       f'coinType CHAR(20) NOT NULL,' \
			       f'status CHAR(10) NOT NULL,' \
			       f'minConfirmations TINYINT NOT NULL,' \
			       f'notice TEXT,' \
			       f'txFee FLOAT,' \
			       f'logoUrl TEXT,' \
			       f'prohibitedIn TEXT,' \
			       f'baseAddress CHAR,' \
			       f'associatedTermsOfService TEXT,' \
			       f'tags TEXT,' \
			       f'PRIMARY KEY (symbol)' \
			       f') ENGINE=Maria'
			cur.execute(comm)
	conn.commit()


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
	for ix in markets:
		with conn.cursor() as cur:
			comm = f'CREATE OR REPLACE TABLE `{ix}` (' \
			       f'symbol CHAR(20) NOT NULL, ' \
			       f'baseCurrencySymbol CHAR(12) NOT NULL, ' \
			       f'quoteCurrencySymbol CHAR(12) NOT NULL, ' \
			       f'minTradeSize FLOAT NOT NULL, ' \
			       f'pprecision TINYINT NOT NULL, ' \
			       f'status CHAR(10) NOT NULL, ' \
			       f'createdAt CHAR(40), ' \
			       f'prohibitedIn TEXT, ' \
			       f'associatedTermsOfService TEXT, ' \
			       f'tags TEXT, ' \
			       f'PRIMARY KEY (symbol)' \
			       f') ENGINE=Maria'
			cur.execute(comm)
	conn.commit()


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
	return True
