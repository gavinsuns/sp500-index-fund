import math #The Python math module
import numpy as np #The Numpy numerical computing library
import pandas as pd #The Pandas data science library
import requests #The requests library for HTTP requests in Python
from secrets import IEX_CLOUD_API_TOKEN
from utils import chunks

stocks = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].values.tolist()
my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']
portfolio_dataframe = pd.DataFrame(columns = my_columns)
symbol_groups = list(chunks(stocks, 100))
symbol_strings = []

for i in range(0, len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))

for symbol_string in symbol_strings:
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch/?types=quote&symbols={symbol_string}&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    for symbol in symbol_string.split(','):
        portfolio_dataframe = pd.concat([portfolio_dataframe,
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

total_rows = len(portfolio_dataframe)

position_size = float(portfolio_size) / total_rows

for i in range(0, total_rows):
    portfolio_dataframe['Number Of Shares to Buy'][i] = math.floor(position_size / portfolio_dataframe['Price'][i])

# create excel sheet
writer = pd.ExcelWriter('sp500.xlsx', engine='xlsxwriter')

# add the portfolio data into the excel sheet
portfolio_dataframe.to_excel(writer, sheet_name='SP500', index = False, na_rep='NaN')

# auto-adjust column widths
for column in portfolio_dataframe:
    column_width = max(portfolio_dataframe[column].astype(str).map(len).max(), len(column))
    col_idx = portfolio_dataframe.columns.get_loc(column)
    writer.sheets['SP500'].set_column(col_idx, col_idx, column_width)

# save the excel file
writer.save()
