import pandas as pd
import datetime
import numpy as np
import requests
from IPython.display import clear_output


def time_to_timestamp(time, last=False):
    """Converts a mm/dd/yyyy formatted time into a unix timestamp including dates before 1/1/1970"""
    epoch = datetime.datetime(1970, 1, 1)  # calculate the epoch timestamp
    month, day, year = time.split("/")  # extract date info from the string
    if last:
        day = str(int(day) + 1)
    t = datetime.datetime(int(year), int(month), int(day))  # Convert the date info to a timestamp
    diff = t - epoch  # Subtract the difference to find how many years, months, and days need to be subtracted/added
    return diff.days * 24 * 60 * 60  # Finding the number of seconds to calculate the timestamp


def total_pct_change(series):
    """Computes the total percentage value change since the origin"""
    values = []
    for i in np.arange(0, len(series)):
        values.append((series[i] / series[0]) - 1)
    return values


def string_to_int(string):
    """Converts short format string values (100M/ 10B) into integers"""
    multipliers = {'K': 1000, 'M': 1000000, 'B': 1000000000, 'T': 1000000000000}
    if pd.isnull(string):
        return np.nan
    if str(string)[-1].isdigit():  # check if no suffix
        return int(string)
    multiplier = multipliers[string[-1].upper()]  # look up suffix to get multiplier
    # convert number to float, multiply by multiplier, then make int
    return int(float(string[:-1]) * multiplier)


def insider_trades(tickers):
    df = pd.DataFrame()
    x = 1
    for i in tickers:
        url = f'http://openinsider.com/screener?s={i}&o=&pl=&ph=&ll=&lh=&fd=1461&fdr=&td=0&tdr=&fdlyl=&fdlyh' \
              '=&daysago=&xp=1&xs=1&xa=1&xd=1&xg=1&xf=1&xm=1&xx=1&xc=1&xw=1&vl=&vh=&ocl=&och=&sic1=-1&sicl' \
              '=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100' \
              '&page='
        for j in range(1, 100):
            tab = pd.read_html(url + str(j))
            if tab[11].columns[1] == 1:
                break
            if len(df[df.duplicated()]) > 0:
                df = df.drop_duplicates()
                break
            df = pd.concat([df, tab[11]])
            clear_output(wait=True)
            print(f"{100 * (x / len(tickers)):.2f}% Complete")
            print(f"Ticker: {i}")
            print(f"{len(df)} Insider Trades Collected")
        x += 1
    df = df.drop(['X', '1d', '1w', '1m', '6m'], axis=1)

    df.columns = ['FilingDate', 'Date', 'Ticker', 'InsiderName', 'Title', 'TradeType', 'Price', 'Qty', 'Owned',
                  'ChangeOwned', 'Value']
    df['Value'] = df['Value'].str.replace(',', '')
    df['Value'] = df['Value'].str.replace('$', '', regex=False).apply(float)

    df['Qty'] = df['Qty'].str.replace('+', '', regex=False)
    df['Qty'] = df['Qty'].str.replace(',', '').apply(float)

    df['Price'] = df['Price'].str.replace(',', '')
    df['Price'] = df['Price'].str.replace('$', '', regex=False).apply(float)
    df['FilingDate'] = pd.to_datetime(df['FilingDate'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('FilingDate')
    df = df.reset_index()
    df  = df.drop(['index'], axis = 1)
    return df


class StockAnalyzer:

    def __init__(self):
        # Defining the url to query
        self.url = "https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1{" \
                   "}&events=history&includeAdjustedClose=true "
        self.header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
                       "X-Requested-With": "XMLHttpRequest"}
        self.screener_url = "https://finviz.com/screener.ashx?v=111"

    def get_price(self,
                  ticker,
                  start='1/1/1900',
                  end=datetime.date.today().strftime('%m/%d/%Y'),
                  freq="d"):
        """Returns the daily stock prices of a single ticker within a defined time range. """
        start = time_to_timestamp(start)
        # End Time
        end = time_to_timestamp(end, last=True)
        stock_price = pd.read_csv(self.url.format(ticker,
                                                  start,
                                                  end,
                                                  freq), index_col=0)

        stock_price['PctChange'] = stock_price['Adj Close'].pct_change()
        stock_price['CumPctChange'] = total_pct_change(stock_price['Adj Close'])

        stock_price['Ticker'] = ticker

        cols = stock_price.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        stock_price = stock_price[cols]

        return stock_price

    def get_prices(self,
                   tickers,
                   start='1/1/1900',
                   end=datetime.date.today().strftime('%m/%d/%Y'),
                   freq="d",
                   debug=False):

        """Returns the daily stock prices of multiple tickers within a defined time range."""
        start = time_to_timestamp(start)
        # End Time
        end = time_to_timestamp(end, last=True)
        df = pd.DataFrame()
        incomplete_list = []

        x = 1
        for i in tickers:
            if debug:
                clear_output(wait=True)
                print("{:.2f}% Complete".format((x / len(tickers)) * 100))
                print(f"Downloading data for {i}")
                x += 1
            try:
                stock_price = pd.read_csv(self.url.format(i,
                                                          start,
                                                          end,
                                                          freq), index_col=0)

                stock_price['PctChange'] = stock_price['Adj Close'].pct_change()
                stock_price['CumPctChange'] = total_pct_change(stock_price['Adj Close'])
                stock_price['Ticker'] = i
                df = pd.concat([df, stock_price])
            except:
                incomplete_list.append(i)
        # Reordering the column names
        cols = df.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        df.index = pd.to_datetime(df.index)
        df = df[cols]
        return df, incomplete_list

    def get_data(self, debug=False):
        """Returns a dataframe containing company name, ticker, industry, sector and market cap"""
        # Create a dataframe to add all the data to
        df = pd.DataFrame()

        # Find the number of stocks by going to the last page and indexing the last stock number
        html_page_text = requests.get('https://finviz.com/screener.ashx?v=111&r=99999', headers=self.header)
        temp = pd.DataFrame(pd.read_html(html_page_text.text, na_values="-")[14])
        temp = temp[1:]
        number_of_stocks = int(temp[0].values)

        # Iterate over all the pages to find all the stocks
        for i in np.arange(1, number_of_stocks, 20):
            self.screener_url = "https://finviz.com/screener.ashx?v=111"
            if debug:
                clear_output(wait=True)
                print("{:.2f}% Complete".format((i / number_of_stocks) * 100))
            self.screener_url = self.screener_url + "&r={}".format(i)
            html_page_text = requests.get(self.screener_url, headers=self.header)
            temp = pd.DataFrame(pd.read_html(html_page_text.text, na_values="-")[14])
            new_header = temp.iloc[0]  # grab the first row for the header
            temp = temp[1:]  # take the data less the header row
            temp.columns = new_header  # set the header row as the df header
            df = pd.concat([df, temp])
        df.index = df['No.']
        df = df.drop(['No.', 'P/E', 'Price', 'Change', 'Volume'], axis=1)
        df['Market Cap'] = df['Market Cap'].apply(string_to_int)
        clear_output(wait=True)
        print("{:.2f}% Complete".format((1 * 100)))
        return df


if __name__ == "__main__":
    stocks = insider_trades(['AAPL', 'TSLA','F','GME','AMC'])
    print(stocks)
