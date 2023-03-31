# Define the book value per share formula
def book_value_per_share(total_shareholder_equity, number_of_shares):
    return total_shareholder_equity / number_of_shares

# Example inputs
total_shareholder_equity = 424899142  # Replace with the actual total shareholder equity of the company
number_of_shares = 64000000  # Replace with the actual number of outstanding shares of the company

# Calculate the book value per share
bvp_share = book_value_per_share(total_shareholder_equity, number_of_shares)
print("The book value per share is:", bvp_share)
