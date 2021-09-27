import backtrader as bt
import datetime

class EMA100Strat(bt.Strategy):

    def __init__(self):
        self.EMA100 = bt.talib.EMA(self.data, timeperiod=100)

    def next(self):
        if self.data < self.EMA100 and not self.position:
            self.buy(size=250000)
        
        if self.data > self.EMA100 and self.position:
            self.close()


cerebro = bt.Cerebro()
cerebro.broker.setcash(100000.0)

data = bt.feeds.GenericCSVData(dataname='Feb-Jul2021_4hREEF.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes)
cerebro.adddata(data)
cerebro.addstrategy(EMA100Strat)

cerebro.run()
cerebro.plot()
