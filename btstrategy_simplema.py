import backtrader as bt

class MovingAverage(bt.Strategy):

	def __init__(self):
		self.order = None

		self.slow_sma =  bt.indicators.MovingAverageSimple(self.datas[0],
							period=50)
		self.fast_sma = bt.indicators.MovingAverageSimple(self.datas[0],
							period=20)

		self.crossover = bt.indicators.CrossOver(self.fast_sma, self.slow_sma)


	def notify_order(self, order):
		if order.status in [order.Submitted, order.Accepted]:
			return

		if order.status in [order.Completed]:
			self.bar_executed = len(self)
		
		self.order = None


	def next(self):
		if self.order:
			return

		if not self.position:
			if self.crossover > 0: # fast crosses above slow
				self.order = self.buy()
			elif self.crossover < 0: # fast crosses below slow
				self.order = self.sell()
		else:
			if len(self) >= (self.bar_executed + 5):
				self.order = self.close()

