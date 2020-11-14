from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Stock(object):
    def __init__(self, ticker, stock_name, start_date, end_date):
        self.ticker = ticker
        self.stock_name = stock_name
        self.start_date = start_date
        self.end_date = end_date
    
    def get_stats(self, stock_data):
        return {
            'last': np.mean(stock_data.tail(1)),
            'short_mean': np.mean(stock_data.tail(20)),
            'long_mean': np.mean(stock_data.tail(200)),
            'short_rolling': stock_data.rolling(window=20).mean(),
            'long_rolling': stock_data.rolling(window=200).mean()
        }

    def create_plot(self, stock_data, stock_name):
        stats = self.get_stats(stock_data)
        plt.xkcd
        plt.subplots(figsize=(12, 8))
        plt.plot(stock_data, label=stock_name)
        plt.plot(stats['short_rolling'], label='20 day rolling mean')
        plt.plot(stats['long_rolling'], label='200 day rolling mean')
        plt.title(self.stock_name)
        plt.legend()
        plt.xlabel('Date')
        plt.ylabel('Adj Close (p)')
        plt.show()
        plt.close()

    def clean_data(self, col):
        weekdays = pd.date_range(start=self.start_date, end=self.end_date)
        clean_data = self.stock_data[col].reindex(weekdays)
        return clean_data.fillna(method='ffill')
    
    def get_data(self):
        try:
            self.stock_data = data.DataReader(self.ticker, 'yahoo', self.start_date, self.end_date)
            adj_close = self.clean_data('Adj Close')
            self.create_plot(adj_close, self.stock_name)
            print(((adj_close[-1] / adj_close[0]) - 1) * 100)

        except RemoteDataError:
            print(f'No data found for {self.ticker}')