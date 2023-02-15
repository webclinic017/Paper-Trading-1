import datetime
import backtrader as bt
from btstrategy_simplema import MovingAverage

TICKER = "F"

cerebro = bt.Cerebro()

cerebro.broker.setcommission(commission=0.001)
cerebro.addsizer(bt.sizers.SizerFix, stake=20)

data = bt.feeds.YahooFinanceCSVData(dataname=f"Yahoo-Data/{TICKER}.csv")
cerebro.adddata(data)

cerebro.addstrategy(MovingAverage)

start_value = cerebro.broker.getvalue()
cerebro.run()
end_value = cerebro.broker.getvalue()

print("Start Value:", start_value)
print("End Value:", end_value)
