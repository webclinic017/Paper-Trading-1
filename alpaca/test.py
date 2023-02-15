from AlpacaTradingInterface import AlpacaTradingAlgo


class Simple(AlpacaTradingAlgo):
    def run(self):
        print("hello")
        print(self.get_current_price('aapl'))
        print("still running")

s = Simple()
s.run()




