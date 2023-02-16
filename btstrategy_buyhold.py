import backtrader as bt

class BuyAndHold(bt.Strategy):

    def __init__(self):
        self.order = None
        self.bought_once = False


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            self.bar_executed = len(self)
        
        self.order = None


    def next(self):
        if self.order:
            return

        if not self.bought_once:
            self.buy()
            self.bought_once = True
