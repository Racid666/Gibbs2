import tkinter as tk

# Define function to calculate Fed Model
def calculate_fed_model():
    earnings = float(earnings_entry.get())
    R10 = float(R10_entry.get())
    earnings_yield = earnings / market_cap
    spread = earnings_yield - R10
    if spread > 0:
        result_label.config(text="Stocks are offering a higher yield than bonds")
    else:
        result_label.config(text="Bonds are offering a higher yield than stocks")
    spread_label.config(text="Spread: {:.2f}%".format(spread*100))

# Create GUI window
root = tk.Tk()
root.title("Fed Model Calculator")

# Create input fields for earnings and R10
earnings_label = tk.Label(root, text="Total earnings of the S&P 500 index:")
earnings_label.pack()
earnings_entry = tk.Entry(root)
earnings_entry.pack()

R10_label = tk.Label(root, text="Yield on the 10-year Treasury bond:")
R10_label.pack()
R10_entry = tk.Entry(root)
R10_entry.pack()

# Create button to calculate Fed Model
calculate_button = tk.Button(root, text="Calculate", command=calculate_fed_model)
calculate_button.pack()

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Create label to display spread
spread_label = tk.Label(root, text="")
spread_label.pack()

# Define market capitalization and Treasury bond rate as constants
market_cap = 4100000000000
R10 = 0.03

# Start GUI
root.mainloop()
