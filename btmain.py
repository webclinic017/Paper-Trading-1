import datetime
import backtrader as bt
from btstrategies import MovingAverage

cerebro = bt.Cerebro()

data = bt.feeds.YahooFinanceCSVData(dataname="AAPL.csv")
cerebro.adddata(data)

cerebro.addstrategy(MovingAverage)

start_value = cerebro.broker.getvalue()
cerebro.run()
end_value = cerebro.broker.getvalue()

print("Start Value:", start_value)
print("End Value:", end_value)
