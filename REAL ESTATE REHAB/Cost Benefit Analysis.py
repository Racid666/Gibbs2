# Define the costs and benefits of the real estate investment
initial_cost = 100000
annual_net_income = 15000
expected_holding_period = 10
resale_value = 250000

# Calculate the total net income from the investment
total_net_income = annual_net_income * expected_holding_period

# Calculate the total benefit from the investment (including resale value)
total_benefit = total_net_income + resale_value

# Calculate the total cost of the investment
total_cost = initial_cost + (annual_net_income * expected_holding_period)

# Calculate the net present value (NPV) of the investment (assuming a discount rate of 5%)
discount_rate = 0.05
npv = -(initial_cost)
for i in range(1, expected_holding_period + 1):
    npv += annual_net_income / ((1 + discount_rate) ** i)
npv += resale_value / ((1 + discount_rate) ** (expected_holding_period + 1))

# Calculate the benefit-cost ratio (BCR) of the investment
bcr = total_benefit / total_cost

# Print the results
print("Total Benefit:", "$" + str(total_benefit))
print("Total Cost:", "$" + str(total_cost))
print("Net Present Value:", "$" + str(round(npv, 2)))
print("Benefit-Cost Ratio:", round(bcr, 2))
