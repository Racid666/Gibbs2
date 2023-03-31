import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objects as go

# Load the stock price data into a Pandas dataframe
df = pd.read_csv('stock_data.csv', index_col='Date', parse_dates=True)

# Define the parameters for the ARIMA model
p = 1 # autoregressive component
d = 1 # integrated component
q = 1 # moving average component

# Fit the ARIMA model to the data
model = ARIMA(df['Close'], order=(p,d,q))
results = model.fit()

# Print the model summary
print(results.summary())

# Get the predicted values and confidence intervals
forecast = results.forecast(steps=365)
forecast_mean = forecast[0]
forecast_upper = forecast[2][:,0]
forecast_lower = forecast[2][:,1]

# Create a Plotly figure for the predicted values and actual values
fig = go.Figure()

fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name='Actual'))
fig.add_trace(go.Scatter(x=forecast_mean.index, y=forecast_mean, name='Predicted'))
fig.add_trace(go.Scatter(x=forecast_upper.index, y=forecast_upper, mode='lines', line=dict(color='gray', width=0), showlegend=False))
fig.add_trace(go.Scatter(x=forecast_lower.index, y=forecast_lower, mode='lines', line=dict(color='gray', width=0), fill='tonexty', showlegend=False))

# Customize the layout of the figure
fig.update_layout(title='ARIMA Model Forecast', xaxis_title='Date', yaxis_title='Closing Price')

# Display the figure
fig.show()

# Plot the predicted values against the actual values using Matplotlib
results.plot_predict(start='2023-01-01', end='2023-03-10')
plt.show()

print(results.converged)
print(len(forecast[0]))
print(df.isna().sum())

