#!/usr/bin/env python3
# Copyright (c) 2021 janmagrot@gmail.com

import requests
import logging
import requests.exceptions

"""
Module for simple data retrieving from Bittrex.com
"""

module_logging = logging.getLogger("bittrex_database." + __name__)
BASEURL = "https://api.bittrex.com/v3/"
false = bool(False)
true = bool(True)
null = None


class PublicApi:
	"""->
	Class handling requests and returns from Bittrex.com.
	"""

	def __init__(self):
		self._logging = logging.getLogger("bittrex_database." + str(__name__) + ".PublicApi()")
		self._logging.info("PublicApi class initiated.")

	@staticmethod
	def __getRaw(method):
		"""
		Method that takes BASEURL + method a send request to Bittrex.com
		servers. Used for encapsulation in excpetions method.
		"""
		request_url = BASEURL + method
		raw = requests.get(request_url, timeout=1.0)
		raw.encoding = 'utf-8'
		return raw

	def __getPublicQueryWrapper(self, method):
		"""
		Queries Bittrex with given method and options.
		:param method:
		:return:
		"""
		sc = None
		raw = None
		try:
			raw = self.__getRaw(method)
			sc = raw.status_code
			if sc != 200:
				raw.raise_for_status()
			else:
				response = raw.json()
				if raw.ok:
					self._logging.debug("Response is presented and succesfull.")
					return response
				else:
					msg = str(response["message"])
					self._logging.error("Connection problems. Response['success'] is negative. Return code is: {}, "
					                    ", meassage from server: {}, Whole response: {}".
					                    format(str(sc), str(msg),
					                           str(response)))
					return False
		except requests.HTTPError:
			self._logging.exception("Connection problem. Status Status code is: {},".format(str(sc)))
			return False
		except requests.ConnectionError:
			self._logging.exception("Connection problem. Status Status code is: {},".format(str(sc)))
			return False
		except ValueError as e:
			self._logging.exception("Problems with decoding data from server. "
			                        "Raw data {}. Details: {}".
			                        format(str(raw.text), str(e.args)))
			return False
		except requests.ReadTimeout:
			self._logging.exception("ReadTimeout.")
			return False
		except requests.Timeout:
			self._logging.exception("Timeout.")
			return False
		except BaseException:
			self._logging.exception("Exception occured")
			return False

	def getAllCurrenciesInfo(self):
		"""
		Get informations about all currencies on Bittrex market.
		"""
		s = self.__getPublicQueryWrapper("currencies")
		return {i["symbol"]: i for i in s}

	def getAllMarketsInfo(self):
		"""
		Get informations about all Bittrex Markets.
		:return:
		"""
		d = self.__getPublicQueryWrapper("markets")
		return {i["symbol"]: i for i in d}

	def getAllMarketsSummaries(self):
		"""
		Return informations about all markets simmaries within
		last 24 hours.
		:return:
		"""
		x = self.__getPublicQueryWrapper("markets/summaries")
		return {i["symbol"]: i for i in x}

	def getAllMarketsTicker(self):
		"""
		Returns ticker for all markets on Bittrex.
		:return:
		"""
		r = self.__getPublicQueryWrapper("markets/tickers")
		return {i["symbol"]: i for i in r}

	def pingBittrex(self):
		"""
		Verification Bittrex.com is online.
		:return:
		"""
		return dict(eval(self.__getRaw("ping").text))
