from alpaca import AlpacaTradingAlgo
from datetime import datetime
from decimal import Decimal
import threading
import time
from alpaca_trade_api.rest import TimeFrame

class LongSimple(AlpacaTradingAlgo):
	def __init__(self):
		super().__init__()
		self.trades = []
		self.holding = False
		self.ticker = 'AAPL'

	def get_mov_avg(self, ticker):
		barset = self.alpaca.get_barset(ticker, '5Min')._raw
		prices = barset[self.ticker]
		total = 0
		for entity in prices:
			total += entity['o']
		return total / len(prices)

	def trade_on_mov_avg(self):
		while True:
			clock = self.alpaca.get_clock()
			if clock.is_open:
				barset = self.alpaca.get_barset(self.ticker, 'minute', limit=1)
				barset = barset._raw
				price = barset[self.ticker][0]['c']
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
						self.trades.append({
							'Action': 'Buy',
							'Time': datetime.now()
						})
						self.holdings[self.ticker] = 6
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
						self.trades.append({
							'Action': 'Sell',
							'Time': datetime.now()
						})
						del self.holdings[self.ticker]
			else:
				# Cancel existing orders
				orders = self.alpaca.list_orders(status="open")
				for order in orders:
					self.alpaca.cancel_order(order.id)
				print("Waiting for the market to open")
			
			# wait a bit
			time.sleep(5)

	def update(self):
		while(True):
			if self.holding:
				print("Holding 6 shares of AAPL")
			else:
				print("Not holding AAPL")
			account = self.alpaca.get_account()._raw
			diff = Decimal(account['portfolio_value']) - 100000
			percent_change = diff / 100000 * 100
			print(f"Account Value Change: {percent_change}", end='\n\n')
			time.sleep(10)

	def run(self):
		mov_avg_thread = threading.Thread(target=self.trade_on_mov_avg)
		mov_avg_thread.start()
		update_thread = threading.Thread(target=self.update)
		update_thread.start()
		

test = LongSimple()
test.run()

