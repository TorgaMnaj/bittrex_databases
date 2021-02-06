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


def createCurrenciesInfoDatabases(currencies):
	"""
	Function that creates tables for informations about
	currencies.
	:param currencies:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database='currenciesinfo')
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


def createMarketsInfoDatabases(markets):
	"""
	Function that creates tables for informations about
	markets.
	:param markets:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database='marketinfo')
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


def createOneMinuteCandles(markets):
	"""
	Function that creates tables for one minute candles.
	:param markets:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database='oneminutecandles')
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


def createFiveMinuteCandles(markets):
	"""
	Function that creates tables for five minute candles.
	:param markets:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database='fiveminutescandles')
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


def createOneHourCandles(markets):
	"""
	Function that creates tables for one minute candles.
	:param markets:
	:return:
	"""
	conn = pymysql.connect(host='localhost',
	                       user='jan',
	                       password='17051982',
	                       database='onehourcandles')
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


s = ['AAPL-BTC', 'AAPL-USD', 'AAPL-USDT', 'AAVE-BTC', 'AAVE-ETH', 'AAVE-EUR', 'AAVE-USD',
     'AAVE-USDT', 'ABBC-BTC', 'ABYSS-BTC', 'ACXT-USDT', 'ADABEAR-USD', 'ADABEAR-USDT', 'ADA-BTC', 'ADABULL-USD',
     'ADABULL-USDT', 'ADA-ETH', 'ADA-EUR', 'ADA-USD', 'ADA-USDT', 'ADK-BTC', 'ADT-BTC', 'ADX-BTC', 'ADX-ETH',
     'AEON-BTC', 'AID-BTC', 'AKN-BTC', 'AKN-USDT', 'AKRO-BTC', 'ALGO-BTC', 'ALGO-USD', 'ALGO-USDT', 'AMC-BTC',
     'AMC-USD', 'AMC-USDT', 'AMP-BTC', 'AMZN-BTC', 'AMZN-USD', 'AMZN-USDT', 'ANKR-BTC', 'ANKR-ETH', 'ANT-BTC',
     'ANT-ETH', 'APM-BTC', 'APM-USDT', 'AR-BTC', 'ARDR-BTC', 'ARK-BTC', 'ATOM-BTC', 'ATOM-ETH', 'ATOM-USD', 'ATOM-USDT',
     'BABA-BTC', 'BABA-USD', 'BABA-USDT', 'BAL-BTC', 'BAL-ETH', 'BAL-EUR', 'BAL-USD', 'BAL-USDT', 'BAND-BTC',
     'BAND-ETH', 'BAND-EUR', 'BAND-USD', 'BAND-USDT', 'BAT-BTC', 'BAT-ETH', 'BAT-USD', 'BAT-USDT', 'BB-BTC', 'BBC-BTC',
     'BBC-USDT', 'BB-USD', 'BB-USDT', 'BCH-BTC', 'BCH-ETH', 'BCH-EUR', 'BCH-USD', 'BCH-USDT', 'BEAR-USD', 'BEAR-USDT',
     'BFT-BTC', 'BILI-BTC', 'BILI-USD', 'BILI-USDT', 'BLK-BTC', 'BLOCK-BTC', 'BNT-BTC', 'BNT-ETH', 'BNTX-BTC',
     'BNTX-USD', 'BNTX-USDT', 'BOA-BTC', 'BOA-USDT', 'BORA-BTC', 'BRZ-BTC', 'BRZ-USDT', 'BSV-BTC', 'BSV-ETH', 'BSV-EUR',
     'BSV-USD', 'BSV-USDT', 'BTC-EUR', 'BTC-USD', 'BTC-USDT', 'BTCV-BTC', 'BTCV-USDT', 'BTE-BTC', 'BTE-USDT', 'BTM-BTC',
     'BTS-BTC', 'BTT-BTC', 'BTT-USDT', 'BTU-BTC', 'BULL-USD', 'BULL-USDT', 'BURST-BTC', 'BWF-BTC', 'BWF-USDT',
     'BWX-BTC', 'BYND-BTC', 'BYND-USD', 'BYND-USDT', 'CAMP-BTC', 'CAMP-USDT', 'CBC-USDT', 'CELO-BTC', 'CELO-ETH',
     'CELO-USD', 'CELO-USDT', 'CGT-BTC', 'CGT-USDT', 'CHR-BTC', 'CKB-BTC', 'CKB-USDT', 'CND-BTC', 'CNS-BTC', 'CNS-USDT',
     'CNTM-BTC', 'CNTM-USDT', 'COMP-BTC', 'COMP-ETH', 'COMP-USD', 'COMP-USDT', 'COSM-BTC', 'CPC-BTC', 'CRO-BTC',
     'CRO-ETH', 'CRO-EUR', 'CRO-USD', 'CRO-USDT', 'CRW-BTC', 'CTC-BTC', 'CTXC-BTC', 'CURE-BTC', 'CUSD-BTC', 'CUSD-USDT',
     'CVC-BTC', 'CVC-ETH', 'CVT-BTC', 'DAI-BTC', 'DAI-ETH', 'DAI-USD', 'DAI-USDT', 'DASH-BTC', 'DASH-ETH', 'DASH-USD',
     'DASH-USDT', 'DAWN-BTC', 'DCR-BTC', 'DCR-USD', 'DCR-USDT', 'DEP-BTC', 'DEP-USDT', 'DFI-BTC', 'DFI-USDT', 'DGB-BTC',
     'DGB-ETH', 'DGB-USD', 'DGB-USDT', 'DMT-BTC', 'DMT-ETH', 'DNA-BTC', 'DNA-USDT', 'DNT-BTC', 'DOGE-BTC', 'DOGE-ETH',
     'DOGE-EUR', 'DOGE-USD', 'DOGE-USDT', 'DOT-BTC', 'DOT-ETH', 'DOT-EUR', 'DOT-USD', 'DOT-USDT', 'DRGN-BTC', 'DTA-BTC',
     'DUCATO-BTC', 'DUSK-BTC', 'ECELL-BTC', 'ECELL-USDT', 'ECOC-BTC', 'ECOC-USDT', 'EDR-BTC', 'ELA-BTC', 'ELAMA-BTC',
     'ELA-USDT', 'EMC2-BTC', 'ENG-BTC', 'ENG-ETH', 'ENJ-BTC', 'ENJ-ETH', 'ENJ-USD', 'ENJ-USDT', 'EOS-BTC', 'EOS-ETH',
     'EOS-USD', 'EOS-USDT', 'ETC-BTC', 'ETC-ETH', 'ETC-USD', 'ETC-USDT', 'ETHBEAR-USD', 'ETHBEAR-USDT', 'ETH-BTC',
     'ETHBULL-USD', 'ETHBULL-USDT', 'ETH-EUR', 'ETH-USD', 'ETH-USDT', 'EXCL-BTC', 'EXE-BTC', 'EXE-USDT', 'EXP-BTC',
     'FB-BTC', 'FB-USD', 'FB-USDT', 'FCT2-BTC', 'FCT-BTC', 'FIL-BTC', 'FIL-ETH', 'FIL-USD', 'FIL-USDT', 'FIRO-BTC',
     'FIT-BTC', 'FLETA-BTC', 'FLO-BTC', 'FME-BTC', 'FME-USDT', 'FNB-BTC', 'FNK-BTC', 'FNK-USDT', 'FOR-BTC', 'FRSP-BTC',
     'FSN-BTC', 'FTC-BTC', 'FX-BTC', 'FX-ETH', 'GAME-BTC', 'GBYTE-BTC', 'GEO-BTC', 'GLEEC-BTC', 'GLM-BTC', 'GLM-ETH',
     'GME-BTC', 'GME-USD', 'GME-USDT', 'GNC-BTC', 'GNC-USDT', 'GNO-BTC', 'GNO-ETH', 'GO-BTC', 'GOLD-USDT', 'GOOGL-BTC',
     'GOOGL-USD', 'GOOGL-USDT', 'GRIN-BTC', 'GRIN-USDT', 'GRS-BTC', 'GRT-BTC', 'GRT-ETH', 'GRT-EUR', 'GRT-USD',
     'GRT-USDT', 'GST-BTC', 'GST-USDT', 'GTO-BTC', 'GXC-BTC', 'GXC-USDT', 'HBAR-BTC', 'HBAR-ETH', 'HBAR-USD',
     'HBAR-USDT', 'HBD-BTC', 'HDAC-BTC', 'HDAO-BTC', 'HDAO-USDT', 'HEDG-BTC', 'HIVE-BTC', 'HIVE-USD', 'HIVE-USDT',
     'HMQ-BTC', 'HNS-BTC', 'HNS-ETH', 'HNS-USDT', 'HXRO-BTC', 'HXRO-USDT', 'HYDRO-BTC', 'ICX-BTC', 'IGNIS-BTC',
     'INSTAR-BTC', 'INX-BTC', 'INX-USDT', 'IOC-BTC', 'IOST-BTC', 'IOTA-BTC', 'IOTX-BTC', 'IRIS-BTC', 'IRIS-USDT',
     'JNT-BTC', 'KAI-BTC', 'KAI-USDT', 'KDA-BTC', 'KDAG-BTC', 'KDAG-USDT', 'KDA-USDT', 'KLAY-BTC', 'KLAY-USDT',
     'KLV-BTC', 'KLV-USDT', 'KMD-BTC', 'KMD-USD', 'KNC-BTC', 'KNC-ETH', 'KNC-EUR', 'KNC-USD', 'KNC-USDT', 'KOK-BTC',
     'KOK-USDT', 'KRT-BTC', 'KRT-USDT', 'KSM-BTC', 'KSM-ETH', 'KSM-USDT', 'LAMB-BTC', 'LBC-BTC', 'LBC-ETH', 'LBC-USD',
     'LBC-USDT', 'LCS-BTC', 'LCS-USDT', 'LINK-BTC', 'LINK-ETH', 'LINK-USD', 'LINK-USDT', 'LMCH-BTC', 'LMCH-USDT',
     'LOOM-BTC', 'LOON-BTC', 'LOON-USDT', 'LRC-BTC', 'LSK-BTC', 'LTC-BTC', 'LTC-ETH', 'LTC-USD', 'LTC-USDT', 'LUCY-BTC',
     'LUCY-USDT', 'LUNA-BTC', 'LUNA-USDT', 'MAID-BTC', 'MANA-BTC', 'MANA-ETH', 'MARO-BTC', 'MATIC-BTC', 'MATIC-USDT',
     'MCH-USDT', 'MDT-BTC', 'MDT-USDT', 'ME-BTC', 'MED-BTC', 'MEME-BTC', 'MER-BTC', 'META-BTC', 'MET-BTC', 'MET-ETH',
     'MFA-BTC', 'MFA-USDT', 'MFT-BTC', 'MKR-BTC', 'MKR-ETH', 'MKR-USDT', 'MOC-BTC', 'MOF-BTC', 'MOF-USDT', 'MONA-BTC',
     'MORE-BTC', 'MRPH-BTC', 'MSTR-BTC', 'MSTR-USD', 'MSTR-USDT', 'MTC-BTC', 'MTL-BTC', 'MUE-BTC', 'MYST-BTC',
     'MYST-USDT', 'NAV-BTC', 'NEO-BTC', 'NEO-ETH', 'NEO-USDT', 'NFLX-BTC', 'NFLX-USD', 'NFLX-USDT', 'NGC-BTC',
     'NKN-BTC', 'NLG-BTC', 'NMR-BTC', 'NMR-ETH', 'NMR-USDT', 'NOK-BTC', 'NOK-USD', 'NOK-USDT', 'NPXS-BTC', 'NPXS-ETH',
     'NPXS-USDT', 'NVT-BTC', 'NVT-USDT', 'NXS-BTC', 'NXT-BTC', 'OCEAN-BTC', 'OCEAN-USDT', 'OGN-BTC', 'OGN-ETH',
     'OGT-BTC', 'OGT-USDT', 'OK-BTC', 'OMG-BTC', 'OMG-ETH', 'OMG-USDT', 'ONG-BTC', 'ONT-BTC', 'ONT-USDT', 'ORBS-BTC',
     'OXEN-BTC', 'OXEN-USDT', 'OXT-BTC', 'OXT-USDT', 'PANDO-USDT', 'PART-BTC', 'PAX-BTC', 'PAX-USD', 'PAY-BTC',
     'PAY-ETH', 'PFE-BTC', 'PFE-USD', 'PFE-USDT', 'PHNX-BTC', 'PHNX-USDT', 'PI-BTC', 'PINK-BTC', 'PIVX-BTC', 'PLA-BTC',
     'PMA-BTC', 'PMA-USDT', 'POT-BTC', 'POWR-BTC', 'POWR-ETH', 'PPC-BTC', 'PROM-BTC', 'PTON-BTC', 'PTOY-BTC', 'PXL-BTC',
     'QLC-BTC', 'QLC-USDT', 'QNT-BTC', 'QRL-BTC', 'QTUM-BTC', 'QTUM-ETH', 'RCN-BTC', 'RDD-BTC', 'REN-BTC', 'RENBTC-BTC',
     'RENBTC-ETH', 'RENBTC-EUR', 'RENBTC-USD', 'RENBTC-USDT', 'REN-ETH', 'REN-EUR', 'REN-USD', 'REN-USDT', 'REPV2-BTC',
     'REPV2-ETH', 'REV-BTC', 'REV-USDT', 'RLC-BTC', 'RVC-BTC', 'RVC-USDT', 'RVN-BTC', 'RVN-USD', 'RVN-USDT',
     'SAND-USDT', 'SBD-BTC', 'SC-BTC', 'SC-ETH', 'SC-USD', 'SC-USDT', 'SDT-BTC', 'SDT-USDT', 'SENSO-BTC', 'SENSO-ETH',
     'SG-BTC', 'SG-USDT', 'SHR-BTC', 'SHR-USDT', 'SIB-BTC', 'SIX-BTC', 'SKM-BTC', 'SKM-USDT', 'SLS-BTC', 'SLV-BTC',
     'SLV-USD', 'SLV-USDT', 'SNT-BTC', 'SNT-ETH', 'SOLVE-BTC', 'SOLVE-ETH', 'SOLVE-USD', 'SOLVE-USDT', 'SPC-BTC',
     'SPHR-BTC', 'SPIN-BTC', 'SPND-BTC', 'SPY-BTC', 'SPY-USD', 'SPY-USDT', 'SQ-BTC', 'SQ-USD', 'SQ-USDT', 'SRN-BTC',
     'SRN-ETH', 'STC-BTC', 'STEEM-BTC', 'STMX-BTC', 'STMX-ETH', 'STORJ-BTC', 'STPT-BTC', 'STRAX-BTC', 'STRAX-ETH',
     'SUKU-BTC', 'SUKU-USDT', 'SUTER-BTC', 'SUTER-USDT', 'SXP-BTC', 'SYS-BTC', 'TEA-BTC', 'TEA-USDT', 'TEMCO-BTC',
     'THC-BTC', 'TNC-BTC', 'TRAC-BTC', 'TRAC-ETH', 'TRAC-USDT', 'TRX-BTC', 'TRX-ETH', 'TRX-EUR', 'TRX-USD', 'TRX-USDT',
     'TRYB-BTC', 'TRYB-USDT', 'TSHP-BTC', 'TSLA-BTC', 'TSLA-USD', 'TSLA-USDT', 'TUBE-BTC', 'TUDA-BTC', 'TUSD-BTC',
     'TUSD-ETH', 'TUSD-USD', 'TUSD-USDT', 'UBQ-BTC', 'UBT-BTC', 'UBT-ETH', 'UCT-BTC', 'UCT-USDT', 'UMA-BTC', 'UMA-ETH',
     'UMA-EUR', 'UMA-USD', 'UMA-USDT', 'UNI-BTC', 'UNI-ETH', 'UNI-USD', 'UNI-USDT', 'UPEUR-BTC', 'UPP-BTC', 'UPT-BTC',
     'UPUSD-BTC', 'UPUSD-USDT', 'UPXAU-BTC', 'UPXAU-USDT', 'UQC-BTC', 'UQC-USDT', 'URAC-BTC', 'USDC-BTC', 'USDC-ETH',
     'USDC-USD', 'USDC-USDT', 'USD-EUR', 'USDN-BTC', 'USDN-USDT', 'USDS-BTC', 'USDS-USD', 'USDT-EUR', 'USDT-USD',
     'UST-BTC', 'UST-USDT', 'UTI-BTC', 'UTK-BTC', 'VAL-BTC', 'VANY-BTC', 'VANY-USDT', 'VBK-BTC', 'VDX-BTC', 'VDX-ETH',
     'VDX-USDT', 'VEE-BTC', 'VET-BTC', 'VET-USDT', 'VIA-BTC', 'VIB-BTC', 'VIB-ETH', 'VID-BTC', 'VITE-BTC', 'VLX-BTC',
     'VLX-USDT', 'VRA-BTC', 'VRC-BTC', 'VTC-BTC', 'WAVES-BTC', 'WAVES-ETH', 'WAXP-BTC', 'WAXP-ETH', 'WAXP-USD',
     'WAXP-USDT', 'WBTC-BTC', 'WBTC-ETH', 'WBTC-USDT', 'WGP-BTC', 'WICC-BTC', 'WICC-USDT', 'WINGS-BTC', 'XDN-BTC',
     'XEM-BTC', 'XEM-ETH', 'XHV-BTC', 'XLM-BTC', 'XLM-ETH', 'XLM-EUR', 'XLM-USD', 'XLM-USDT', 'XMR-BTC', 'XMR-ETH',
     'XMR-USDT', 'XMY-BTC', 'XRP-BTC', 'XRP-ETH', 'XRP-EUR', 'XRP-USD', 'XRP-USDT', 'XST-BTC', 'XTP-BTC', 'XTZ-BTC',
     'XTZ-ETH', 'XTZ-USD', 'XTZ-USDT', 'XUC-BTC', 'XUC-USDT', 'XVG-BTC', 'XVG-USDT', 'XWC-BTC', 'XWC-USDT', 'YFL-BTC',
     'YFL-ETH', 'YFL-EUR', 'YFL-USD', 'YFL-USDT', 'YOU-BTC', 'ZEC-BTC', 'ZEC-ETH', 'ZEC-USD', 'ZEC-USDT', 'ZEN-BTC',
     'ZEN-USD', 'ZIL-BTC', 'ZRX-BTC', 'ZRX-ETH', 'ZRX-USD', 'ZRX-USDT']

createOneMinuteCandles(s)
createFiveMinuteCandles(s)
createOneHourCandles(s)
