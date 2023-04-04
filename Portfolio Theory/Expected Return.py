import yfinance as yf
import pandas as pd
import numpy as np

# Replace 'AAPL' with the stock symbol you want to evaluate
stock_symbol = 'MRC'

# Download historical stock data
stock_data = yf.download(stock_symbol, start='2022-01-01', end='2023-01-01')

# Calculate daily returns
stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()
print(dir(stock_data))
# Calculate average daily return
average_daily_return = stock_data['Daily Return'].mean()

# Calculate annualized return
annualized_return = (1 + average_daily_return) ** 252 - 1

# Print expected return
print(f"The expected annualized return for {stock_symbol} is: {annualized_return * 100:.2f}%")
