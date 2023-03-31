import pandas_datareader as pdr
import yfinance as yfin


# yfin.pdr_override()

# Define the stock ticker symbol
ticker = 'AAPL'

# Define the start and end dates for the period of analysis
start_date = '2023-01-01'
end_date = '2023-01-31'

#  note - GSPC fixed to ^GSPC ...
#  Use the Pandas DataReader to retrieve the stock price data and the S&P 500 price data for the same period
index_data = yfin.download('^GSPC', start=start_date, end=end_date)
stock_data = yfin.download(ticker, start=start_date, end=end_date)
# index_data = pdr.get_data_yahoo('^GSPC', start_date, end_date)

# Calculate the daily returns for the stock and the index
stock_returns = stock_data['Adj Close'].pct_change()
index_returns = index_data['Adj Close'].pct_change()

# Define the risk-free rate (as a decimal)
risk_free_rate = 0.01

# Calculate the stock's beta using linear regression
covariance = stock_returns.cov(index_returns)
variance = index_returns.var()
beta = covariance / variance

# Calculate the expected market return and the expected stock return
expected_market_return = index_returns.mean()
expected_stock_return = risk_free_rate + beta * (expected_market_return - risk_free_rate)

# Calculate the actual stock return over the period of analysis
actual_stock_return = (stock_data['Adj Close'][-1] / stock_data['Adj Close'][0]) - 1

# Calculate the alpha
alpha = actual_stock_return - expected_stock_return

print(f"The alpha of {ticker} for the period from {start_date} to {end_date} is: {alpha:.4f}")