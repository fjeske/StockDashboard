from datetime import datetime
from create_stock import Stock


def main():
    tickers = ['APC.DE', 'AMZ.DE']

    #creates an object of a stock
    apple = Stock(ticker=tickers[0], stock_name='Apple', start_date='2019-01-14', end_date=str(datetime.now().strftime('%Y-%m-%d')))
    amazon = Stock(ticker=tickers[0], stock_name='Amazon', start_date='2019-01-14', end_date=str(datetime.now().strftime('%Y-%m-%d')))

    apple.get_data()
    amazon.get_data()



    # for ticker in tickers:
    #     get_data(ticker)

if __name__ == "__main__":
    main()