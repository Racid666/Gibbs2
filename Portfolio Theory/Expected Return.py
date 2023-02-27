import numpy as np

# For a PORTFOLIO of ASSETS.

# Define the asset returns and weights
asset_returns = np.array([0.05, 0.08, 0.12, 0.10])
weights = np.array([0.2, 0.3, 0.4, 0.1])

# Calculate the expected return
expected_return = np.dot(asset_returns, weights)

print("The expected return of the portfolio is:", expected_return)