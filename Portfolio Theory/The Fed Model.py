import pandas as pd
import matplotlib.pyplot as plt

# Define the Fed Model formula
def fed_model(earnings_yield, treasury_yield):
    return earnings_yield - treasury_yield

# Load the Treasury yield curve data from a CSV file
treasury_data = pd.read_csv("treasury_yield_curve.csv", index_col=0)

# Define the maturities to use for the analysis (in years)
maturities = [2, 5, 10, 30]

# Plot the Treasury yield curve
for maturity in maturities:
    plt.plot(treasury_data.index, treasury_data[str(maturity) + " YR"], label=str(maturity) + " Year")

plt.title("Treasury Yield Curve")
plt.xlabel("Date")
plt.ylabel("Yield")
plt.legend()
plt.show()

# Load the earnings data for a stock
earnings_yield = 0.05  # Replace with the actual earnings yield for the stock

# Calculate the difference between the earnings yield and the Treasury yield for each maturity
fed_model_values = {}
for maturity in maturities:
    treasury_yield = treasury_data[str(maturity) + " YR"].iloc[-1] / 100
    fed_model_values[str(maturity) + " Year"] = fed_model(earnings_yield, treasury_yield)

# Plot the results of the Fed Model analysis
plt.bar(fed_model_values.keys(), fed_model_values.values())
plt.title("Fed Model Analysis")
plt.xlabel("Maturity")
plt.ylabel("Earnings Yield - Treasury Yield")
plt.show()
