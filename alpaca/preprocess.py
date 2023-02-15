import sys
import re
from config import API_KEY, SECRET_KEY, APCA_API_BASE_URL
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame


def get_data(ticker, year=2018):
    stock_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
    request_params = StockBarsRequest(symbol_or_symbols=[ticker],
                                        start=
                                        )
    bars = stock_client.get_stock_bars(request_params)
    return bars


if __name__=="__main__":
    bars = get_data("AAPL")
    print(bars.df)


class Preprocess:
    def __init__(self):
        self.raw_data = []


    def read_file(self):
        for line in sys.stdin:
            line = line.rstrip()
            date, close, volume, open, high, low = line.split(',')
            close = re.sub(r'\W+', '', close)
            open = re.sub(r'\W+', '', open)
            high = re.sub(r'\W+', '', high)
            low = re.sub(r'\W+', '', low)
            day_info = {
                'date': date,
                'close': close,
                'volume': volume,
                'open': open,
                'high': high,
                'low': low
            }
            self.raw_data.append(day_info)

    
    def mark_data(self):
        pass
        


