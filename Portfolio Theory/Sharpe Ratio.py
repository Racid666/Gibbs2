import numpy as np

# Define the expected portfolio return, risk-free rate and portfolio standard deviation
expected_return = 0.10
risk_free_rate = 0.03
portfolio_std_dev = 0.15

# Calculate the Sharpe Ratio
sharpe_ratio = (expected_return - risk_free_rate) / portfolio_std_dev

# Print the result
print("The Sharpe Ratio of the portfolio is:", sharpe_ratio)
