import backtrader as bt
import random

class Random(bt.Strategy):

    def __init__(self):
        self.order = None
        random.seed(1)


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
            num = random.randint(1,2)
            if num == 1:
                self.order = self.buy()
            else:
                self.order = self.sell()
        else:
            if len(self) >= (self.bar_executed + 5):
                self.order = self.close()

