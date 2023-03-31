import tkinter as tk

# Define the Discounted Payback Period function
def calculate_discounted_payback_period(initial_investment, cash_flows, discount_rate):
    cumulative_cash_flows = 0
    for i, cash_flow in enumerate(cash_flows):
        cumulative_cash_flows += cash_flow / ((1 + discount_rate) ** i)
        if cumulative_cash_flows >= initial_investment:
            return i + (initial_investment - (cumulative_cash_flows - cash_flow / ((1 + discount_rate) ** i))) / (cash_flow / ((1 + discount_rate) ** i))
    return None

# Define the GUI
root = tk.Tk()
root.title("Discounted Payback Period Calculator")

# Define the input fields
initial_investment_label = tk.Label(root, text="Initial Investment:")
initial_investment_entry = tk.Entry(root)
cash_flows_label = tk.Label(root, text="Cash Flows (comma-separated):")
cash_flows_entry = tk.Entry(root)
discount_rate_label = tk.Label(root, text="Discount Rate:")
discount_rate_entry = tk.Entry(root)

# Define the output field
discounted_payback_period_label = tk.Label(root, text="Discounted Payback Period: N/A")

# Define the calculate button
def calculate_discounted_payback_period_callback():
    initial_investment = float(initial_investment_entry.get())
    cash_flows = [float(x.strip()) for x in cash_flows_entry.get().split(",")]
    discount_rate = float(discount_rate_entry.get())
    discounted_payback_period = calculate_discounted_payback_period(initial_investment, cash_flows, discount_rate)
    if discounted_payback_period is None:
        discounted_payback_period_label.config(text="Discounted Payback Period: N/A")
    else:
        discounted_payback_period_label.config(text="Discounted Payback Period: " + str(round(discounted_payback_period, 2)) + " years")

calculate_button = tk.Button(root, text="Calculate", command=calculate_discounted_payback_period_callback)

# Arrange the widgets using the grid layout manager
initial_investment_label.grid(row=0, column=0)
initial_investment_entry.grid(row=0, column=1)
cash_flows_label.grid(row=1, column=0)
cash_flows_entry.grid(row=1, column=1)
discount_rate_label.grid(row=2, column=0)
discount_rate_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)
discounted_payback_period_label.grid(row=4, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()
