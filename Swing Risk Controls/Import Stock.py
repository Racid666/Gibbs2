import yfinance as yf

# Define the stock symbol and date range
symbol = 'BMA'
start_date = '2014-01-01'
end_date = '2020-08-23'

# Retrieve the historical price data from Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

# Save the historical price data to a CSV file
filename = f"{symbol}.csv"
data.to_csv(filename)
print(f"Saved {filename} to disk.")