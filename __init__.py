from abc import ABC, abstractmethod


class Trade(ABC):
    def __init__(self):
        self.holdings = {}

    @abstractmethod
    def trade(self, symbol, qty, side, type='market', time_in_force='gtc'):
        pass

    @abstractmethod
    def get_current_price(symbol):
        pass

    @abstractmethod
    def liquidate_all():
        pass