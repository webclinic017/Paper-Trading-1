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

    
    def mark_data


test = Preprocess()
test.run()