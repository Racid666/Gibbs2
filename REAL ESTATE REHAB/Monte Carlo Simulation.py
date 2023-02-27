import numpy as np

# Define the inputs for the Monte Carlo Simulation
initial_investment = 100000
expected_return = 0.10
expected_volatility = 0.20
holding_period = 10
simulations = 1000

# Generate random simulations of the expected returns for each year of the holding period
returns = np.random.normal(loc=expected_return, scale=expected_volatility, size=(simulations, holding_period))

# Calculate the future value of the investment for each simulation
future_values = []
for i in range(simulations):
    future_value = initial_investment
    for j in range(holding_period):
        future_value *= 1 + returns[i, j]
    future_values.append(future_value)

# Calculate the expected future value of the investment
expected_future_value = np.mean(future_values)

# Calculate the 5th percentile and 95th percentile of the future values
lower_bound = np.percentile(future_values, 5)
upper_bound = np.percentile(future_values, 95)

# Print the results
print("Expected Future Value:", "$" + str(round(expected_future_value, 2)))
print("5th Percentile Future Value:", "$" + str(round(lower_bound, 2)))
print("95th Percentile Future Value:", "$" + str(round(upper_bound, 2)))
