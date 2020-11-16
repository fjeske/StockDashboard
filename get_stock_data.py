from datetime import datetime
from create_stock import Stock
from settings import tickers

def main():
    stocks = {}
    for ticker in tickers:
        print(ticker)
        print(tickers[ticker])

        #creates an object of a stock
        stocks[f"{ticker}"] = Stock(ticker=tickers[ticker], stock_name=ticker, start_date='2019-01-14', end_date=str(datetime.now().strftime('%Y-%m-%d')))

        stocks[ticker].get_data()

if __name__ == "__main__":
    main()