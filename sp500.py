from distutils.log import error
import math #The Python math module
import numpy as np #The Numpy numerical computing library
import pandas as pd #The Pandas data science library
import requests #The requests library for HTTP requests in Python
import xlsxwriter #The XlsxWriter libarary for
from secrets import IEX_CLOUD_API_TOKEN
from utils import chunks

stocks = pd.read_csv('sp_500_stocks.csv')
stocks = stocks[~stocks['Ticker'].isin(['DISCA', 'HFC','VIAC','WLTW'])]
my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
symbol_groups = list(chunks(stocks['Ticker'], 100))
symbol_strings = []

for i in range(0, len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))

for symbol_string in symbol_strings:
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch/?types=quote&symbols={symbol_string}&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    for symbol in symbol_string.split(','):
        final_dataframe = pd.concat([final_dataframe,
                                        pd.DataFrame([[symbol, 
                                                   data[symbol]['quote']['latestPrice'], 
                                                   data[symbol]['quote']['marketCap'], 
                                                   'N/A']], 
                                                  columns = my_columns)], 
                                        ignore_index = True)

while True:
    try:
        portfolio_size = input('Enter the value of your portfolio:')
        val = float(portfolio_size)
        break
    except ValueError:
        print('That\'s not a number! \n Try again:')

total_rows = len(final_dataframe)
position_size = float(portfolio_size) / total_rows
for i in range(0, total_rows):
    final_dataframe['Number Of Shares to Buy'][i] = math.floor(position_size / final_dataframe['Price'][i])
