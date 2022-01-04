import sys
import re

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
                        self.trades.append({
                            'Action': 'Buy',
                            'Time': datetime.now()
                        })
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
            else:
                # Cancel existing orders
                orders = self.alpaca.list_orders(status="open")
                for order in orders:
                    self.alpaca.cancel_order(order.id)
                print("Waiting for the market to open")
            
            # wait a bit
            time.sleep(5)
        


test = Preprocess()
test.run()