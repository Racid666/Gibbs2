import numpy as np

# Define the returns for two assets
asset1_returns = np.array([0.05, 0.08, 0.12, 0.10, 0.06])
asset2_returns = np.array([0.02, 0.04, 0.10, 0.12, 0.08])

# Calculate the mean returns
mean1 = np.mean(asset1_returns)
mean2 = np.mean(asset2_returns)

# Calculate the deviations from the mean
dev1 = asset1_returns - mean1
dev2 = asset2_returns - mean2

# Calculate the covariance
covariance = np.dot(dev1, dev2) / (len(asset1_returns) - 1)

print("The covariance between the two assets is:", covariance)
