import datetime
import threading
from config import *

import alpaca_trade_api as tradeapi
import time
from alpaca_trade_api.rest import TimeFrame

class LongSimple:
	def __init__(self):
		self.alpaca = tradeapi.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL, 'v2')

	def run(self):
		# Cancel existing orders
		orders = self.alpaca.list_orders(status="open")
		for order in orders:
			self.alpaca.cancel_order(order.id)
		print("Waiting for the market to open")
		
		


test = LongSimple()
test.run()

