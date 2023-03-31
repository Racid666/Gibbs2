import pandas as pd
import numpy as np
import statsmodels.api as sm

# Define the stock symbol and date range
symbol = 'MRC'
start_date = '2022-01-01'
end_date = '2023-02-27'

# Define the benchmark symbol and date range
benchmark = '^GSPC'  # S&P 500 index
benchmark_start_date = '2018-01-01'
benchmark_end_date = '2022-12-31'

# Retrieve the historical price data from Yahoo Finance
stock_data = pd.DataFrame()
benchmark_data = pd.DataFrame()

try:
    stock_data = pd.read_csv(f"{symbol}.csv", index_col='Date', parse_dates=True)
    benchmark_data = pd.read_csv(f"{benchmark}.csv", index_col='Date', parse_dates=True)
except FileNotFoundError:
    stock_data = pd.DataFrame(yf.download(symbol, start=start_date, end=end_date))
    benchmark_data = pd.DataFrame(yf.download(benchmark, start=benchmark_start_date, end=benchmark_end_date))

# Calculate the daily returns of the stock and the benchmark
stock_returns = np.log(stock_data['Close'] / stock_data['Close'].shift(1))
benchmark_returns = np.log(benchmark_data['Close'] / benchmark_data['Close'].shift(1))

# Calculate the excess returns of the stock
excess_returns = stock_returns - benchmark_returns

# Run a regression analysis of the excess returns
X = sm.add_constant(benchmark_returns)
model = sm.OLS(excess_returns, X, missing='drop')
results = model.fit()

# Get the alpha coefficient
alpha = results.params[0]

# Print the results
print(f"Stock: {symbol}")
print(f"Benchmark: {benchmark}")
print(f"Alpha: {alpha:.4f}")
print(f"R-squared: {results.rsquared:.4f}")
print(f"Adjusted R-squared: {results.rsquared_adj:.4f}")
