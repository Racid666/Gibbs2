# Import necessary libraries
import numpy as np

# Define inputs
risk_free_rate = 0.03
market_return = 0.12
beta = 1.5

# Calculate expected return using CAPM formula
expected_return = risk_free_rate + beta * (market_return - risk_free_rate)

# Print the result
print("The expected return of the portfolio using the CAPM formula is:", expected_return)
