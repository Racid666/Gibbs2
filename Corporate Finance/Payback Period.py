import tkinter as tk

# Define the Payback Period function
def calculate_payback_period(initial_investment, cash_flows):
    cumulative_cash_flows = 0
    for i, cash_flow in enumerate(cash_flows):
        cumulative_cash_flows += cash_flow
        if cumulative_cash_flows >= initial_investment:
            return i + (initial_investment - (cumulative_cash_flows - cash_flow)) / cash_flow
    return None

# Define the GUI
root = tk.Tk()
root.title("Payback Period Calculator")

# Define the input fields
initial_investment_label = tk.Label(root, text="Initial Investment:")
initial_investment_entry = tk.Entry(root)
cash_flows_label = tk.Label(root, text="Cash Flows (comma-separated):")
cash_flows_entry = tk.Entry(root)

# Define the output field
payback_period_label = tk.Label(root, text="Payback Period: N/A")

# Define the calculate button
def calculate_payback_period_callback():
    initial_investment = float(initial_investment_entry.get())
    cash_flows = [float(x.strip()) for x in cash_flows_entry.get().split(",")]
    payback_period = calculate_payback_period(initial_investment, cash_flows)
    if payback_period is None:
        payback_period_label.config(text="Payback Period: N/A")
    else:
        payback_period_label.config(text="Payback Period: " + str(round(payback_period, 2)) + " years")

calculate_button = tk.Button(root, text="Calculate", command=calculate_payback_period_callback)

# Arrange the widgets using the grid layout manager
initial_investment_label.grid(row=0, column=0)
initial_investment_entry.grid(row=0, column=1)
cash_flows_label.grid(row=1, column=0)
cash_flows_entry.grid(row=1, column=1)
calculate_button.grid(row=2, column=0, columnspan=2)
payback_period_label.grid(row=3, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()
