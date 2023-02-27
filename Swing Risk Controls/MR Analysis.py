import pandas as pd


# Load historical price data for a stock
symbol = 'BMA'
data = pd.read_csv(f'{symbol}.csv', index_col='Date', parse_dates=True)['Close']


def mean_reversion(data, lookback_period, deviation):
    """Identify mean reversion opportunities for a stock based on a lookback period and deviation threshold"""

    # Calculate rolling mean and standard deviation
    rolling_mean = data.rolling(window=lookback_period).mean()
    rolling_std = data.rolling(window=lookback_period).std()

    # Calculate upper and lower deviation thresholds
    upper_band = rolling_mean + deviation * rolling_std
    lower_band = rolling_mean - deviation * rolling_std

    # Identify mean reversion opportunities
    is_above_upper_band = data > upper_band
    is_below_lower_band = data < lower_band
    is_mean_reversion = (is_above_upper_band.shift(1) & is_below_lower_band.shift(1))

    return is_mean_reversion

# Calculate mean reversion opportunities
lookback_period = 2200
deviation = 2
is_mean_reversion = mean_reversion(data, lookback_period, deviation)

# Print summary statistics
print(f"Mean reversion opportunities for {symbol}:")
print(is_mean_reversion.describe())
