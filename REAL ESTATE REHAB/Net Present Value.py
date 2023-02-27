# Define the cash flows for the real estate investment
cash_flows = [-50000, 10000, 15000, 20000, 25000, 30000]

# Define the discount rate
discount_rate = 0.08

# Calculate the NPV
npv = 0
for i, cash_flow in enumerate(cash_flows):
    npv += cash_flow / ((1 + discount_rate) ** i)

# Print the result
print("The Net Present Value of the real estate investment is:", round(npv, 2))
