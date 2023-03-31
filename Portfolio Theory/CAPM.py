# Import necessary libraries
import numpy as np

# Define inputs
risk_free_rate = 3.95
market_return = -5.3
beta = 2.17

# Calculate expected return using CAPM formula
expected_return = risk_free_rate + beta * (market_return - risk_free_rate)

# Print the result
print("The expected return of the portfolio using the CAPM formula is:", expected_return)
