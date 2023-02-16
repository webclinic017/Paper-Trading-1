import datetime
import backtrader as bt
from btstrategy_simplema import MovingAverage
from btstrategy_buyhold import BuyAndHold

TICKER = "F"
STRATEGY = MovingAverage

if __name__ == "__main__":

    strategies = {
        "Buy and Hold": BuyAndHold,
        "You Selected": STRATEGY
    }

    for strategy_name in strategies:
        print("Results for:", strategy_name)

        cerebro = bt.Cerebro()

        cerebro.broker.setcommission(commission=0.001)
        cerebro.addsizer(bt.sizers.SizerFix, stake=50)

        data = bt.feeds.YahooFinanceCSVData(dataname=f"Yahoo-Data/{TICKER}.csv")
        cerebro.adddata(data)

        cerebro.addstrategy(strategies[strategy_name])

        start_value = cerebro.broker.getvalue()
        cerebro.run()
        end_value = cerebro.broker.getvalue()

        print("Start Value:", start_value)
        print("End Value:", end_value)
        print("")
