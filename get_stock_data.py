from datetime import datetime
from create_stock import Stock


def main():
    tickers = ['APC.DE', 'AMZ.DE', 'SRB.DE']

    #creates an object of a stock
    apple = Stock(ticker=tickers[0], stock_name='Apple', start_date='2019-01-14', end_date=str(datetime.now().strftime('%Y-%m-%d')))
    amazon = Stock(ticker=tickers[1], stock_name='Amazon', start_date='2019-01-14', end_date=str(datetime.now().strftime('%Y-%m-%d')))
    starbucks = Stock(ticker=tickers[2], stock_name='Starbucks', start_date='2019-01-14', end_date=str(datetime.now().strftime('%Y-%m-%d')))

    apple.get_data()
    amazon.get_data()
    starbucks.get_data()



    # for ticker in tickers:
    #     get_data(ticker)

if __name__ == "__main__":
    main()