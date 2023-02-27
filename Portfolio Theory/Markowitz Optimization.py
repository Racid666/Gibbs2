import numpy as np
from scipy.optimize import minimize

# Define the expected returns and covariance matrix for the assets
returns = np.array([0.05, 0.08, 0.12])
covariance_matrix = np.array([[0.05, 0.02, 0.01],
                              [0.02, 0.10, 0.05],
                              [0.01, 0.05, 0.15]])

# Define the objective function to be minimized
def portfolio_variance(weights, returns, covariance_matrix):
    portfolio_return = np.dot(weights, returns)
    portfolio_variance = np.dot(weights.T, np.dot(covariance_matrix, weights))
    return portfolio_variance

# Define the constraints
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# Define the bounds
bounds = tuple((0, 1) for i in range(3))

# Define the initial guess for the weights
initial_guess = [1/3, 1/3, 1/3]

# Perform the optimization
result = minimize(portfolio_variance, initial_guess, args=(returns, covariance_matrix), method='SLSQP', bounds=bounds, constraints=constraints)

# Print the results
print("Optimal weights:", result.x)
print("Minimum variance:", result.fun)