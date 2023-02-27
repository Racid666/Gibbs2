# Define the sales prices of comparable properties
comparable_sales = [200000, 225000, 190000, 215000, 205000]

# Calculate the average sales price of the comparable properties
average_sales_price = sum(comparable_sales) / len(comparable_sales)

# Estimate the value of the subject property based on the average sales price
subject_property_value = average_sales_price

# Print the result
print("Based on the Comparable Sales Analysis, the estimated value of the subject property is:", "$" + str(subject_property_value))
