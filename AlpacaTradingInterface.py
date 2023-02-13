from config import API_KEY, SECRET_KEY, APCA_API_BASE_URL
from abc import ABC, abstractmethod
from __init__ import Trade
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
from datetime import datetime
from datetime import timedelta
import pandas as pd


class AlpacaTradingAlgo(Trade):
    def __init__(self):
        self.alpaca = tradeapi.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL, 'v2')

    @abstractmethod
    def run(self):
        pass

    def trade(self, symbol, qty, side, type='market', time_in_force='gtc'):
        self.alpaca.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,
            time_in_force=time_in_force
        )

    def get_current_price(self, symbol):
        print(pd.Timestamp('now').date() - timedelta(days=1))
        bars = self.alpaca.get_bars(symbol, TimeFrame.Day,
                            pd.Timestamp('now').date() - timedelta(days=1),
                            pd.Timestamp('now').date() - timedelta(days=1), limit=1,
                            adjustment='raw')
        print(bars)
        return bars[0].c

    def liquidate_all(self):
        for ticker, share_count in self.holdings.items():
            self.alpaca.submit_order(
                symbol=ticker,
                qty=share_count,
                side='sell',
                type='market',
                time_in_force='gtc'
            )

    
