import pandas as pd
import arch

# Load the stock price data into a Pandas dataframe
df = pd.read_csv('stock_data.csv', index_col='Date', parse_dates=True)

# Create an instance of the GARCH model
garch_model = arch.arch_model(df['Close'], vol='GARCH', p=1, q=1)

# Fit the GARCH model to the data
results = garch_model.fit()

# Print the model summary
print(results.summary())

# Generate a forecast for the next 30 days
forecast = results.forecast(horizon=30)
print(forecast.mean.iloc[-1])
