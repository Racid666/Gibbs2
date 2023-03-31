import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load GDP data
gdp_data = pd.read_csv('gdp_data.csv')
gdp_data = gdp_data.rename(columns={'GDP': 'gdp_data', 'date': 'date'})

# Load inflation data
inflation_data = pd.read_csv('inflation_data.csv')
inflation_data = inflation_data.rename(columns={'inflation': 'inflation_data', 'date': 'date'})

# Merge data on date column
data = pd.merge(gdp_data, inflation_data, on='date')

# Load stock data
stock_data = pd.read_csv('stock_data.csv')

# Merge data on date column
data = pd.merge(data, stock_data, on='date')

# Impute missing values with mean
data = data.fillna(data.mean())

# Define variables
y = data['Close']
X = data[['gdp_data', 'inflation_data']]

# Add intercept term
X = sm.add_constant(X)

# Print shapes of input arrays
print("Shape of y:", y.shape)
print("Shape of X:", X.shape)

# Fit regression model
model = sm.OLS(y, X).fit()

# Print regression results
print(model.summary())
