#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime


class Stock():
    """
    Model for stock. Store it's code, type, last dividend value, par value, fixed dividend.
    Counts dividend yield, pe_ratio.
    """
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, d):
        if not d:
            raise Exception("Code cannot be empty")
        self._code = str(d)
        
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, d):
        if not d:
            raise Exception("Type cannot be empty")
        self._type = str(d)   

    @property
    def last_dividend(self):
        return self._last_dividend

    @last_dividend.setter
    def last_dividend(self, d):
        if not d:
            raise Exception("last_dividend cannot be empty")
        self._last_dividend = int(d)
        
    @property
    def par_values(self):
        return self._par_values

    @par_values.setter
    def par_values(self, d):
        if not d:
            raise Exception("par_values cannot be empty")
        self._par_values = int(d)

    @property
    def fixed_dividend(self):
        return self._fixed_dividend

    @fixed_dividend.setter
    def fixed_dividend(self, d):
        if not d:
            raise Exception("fixed_dividend cannot be empty")
        self._fixed_dividend = int(d)

    def __init__(self, code, type, last_dividend, par_value, fixed_dividend=None):

        self.code = code
        self.type = type
        self.last_dividend = last_dividend
        self.par_value = par_value
        self.fixed_dividend = fixed_dividend

    def dividend_yield(self):
        """
        Counting dividend yield in two ways. Depends on type of stock.
        :return:
        """
        if self.type == 'Common':
            return self.last_dividend / ticker_price
        elif self.type == 'Preffered':
            return self.fixed_dividend * self.par_value / ticker_price

    def pe_ratio(self):
        return ticker_price / self.last_dividend

class Trade():
    """
    Model for a trade. Records timestamp, buy or sell indicator, quantity and price.
    """
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, d):
        if not d:
            raise Exception("timestamp cannot be empty")
        self._timestamp = str(d)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, d):
        if not d:
            raise Exception("quantity cannot be empty")
        self._quantity = str(d)

    @property
    def buy_or_sell(self):
        return self._buy_or_sell

    @buy_or_sell.setter
    def buy_or_sell(self, d):
        if not d:
            raise Exception("buy_or_sell cannot be empty")
        self._buy_or_sell = int(d)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, d):
        if not d:
            raise Exception("price cannot be empty")
        self._price = int(d)

    def __init__(self, quantity, buy_or_sell, price):

        self.quantity = quantity
        self.buy_or_sell = buy_or_sell
        self.price = price

        self.timestamp = datetime.datetime.now()


class Trades():
    """
    Model to handle all trade records. Counting Stock price and GBCE
    """
     def __init__(self):

        self.records = []

    def get_stock_price():
        last_records = self.records[-15:]

        self.trade_price(last_records)
        self.quantity(last_records)