import datetime
import threading
from config import *

import alpaca_trade_api as tradeapi
import time
from alpaca_trade_api.rest import TimeFrame

class LongSimple:
	def __init__(self):
		self.alpaca = tradeapi.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL, 'v2')
		self.trades = []
		self.holding = False
		self.ticker = 'AAPL'

	def get_mov_avg(self, ticker):
		barset = self.alpaca.get_barset(ticker, '5Min')
		total = 0
		for entity in barset:
			total += entity['o']
		return total / len(barset)

	def run(self):
		while True:
			clock = self.alpaca.get_clock()
			if clock.is_open:
				barset = self.alpaca.get_barset(self.ticker, 'minute', limit=1)
				price = barset[0].o
				if price <= self.get_mov_avg(self.ticker):
					if not self.holding:
						self.alpaca.submit_order(
							symbol=self.ticker,
							qty=6,
							side='buy',
							type='market',
							time_in_force='gtc'
						)
						self.holding = True
				else:
					if self.holding:
						self.alpaca.submit_order(
							symbol=self.ticker,
							qty=6,
							side='sell',
							type='market',
							time_in_force='gtc'
						)
						self.holding = False
			else:
				# Cancel existing orders
				orders = self.alpaca.list_orders(status="open")
				for order in orders:
					self.alpaca.cancel_order(order.id)
				print("Waiting for the market to open")
			
			# wait a bit
			time.sleep(5)
		


test = LongSimple()
test.run()

