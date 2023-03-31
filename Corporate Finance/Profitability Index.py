import tkinter as tk

# Define the Profitability Index function
def calculate_pi(initial_investment, cash_flows, discount_rate):
    present_value_cash_flows = [cash_flow / ((1 + discount_rate) ** n) for n, cash_flow in enumerate(cash_flows)]
    present_value_sum = sum(present_value_cash_flows)
    return present_value_sum / initial_investment

# Define the GUI
root = tk.Tk()
root.title("Profitability Index Calculator")

# Define the input fields
initial_investment_label = tk.Label(root, text="Initial Investment:")
initial_investment_entry = tk.Entry(root)
cash_flows_label = tk.Label(root, text="Cash Flows (comma-separated):")
cash_flows_entry = tk.Entry(root)
discount_rate_label = tk.Label(root, text="Discount Rate:")
discount_rate_entry = tk.Entry(root)

# Define the output field
pi_label = tk.Label(root, text="Profitability Index: 0")

# Define the calculate button
def calculate_pi_callback():
    initial_investment = float(initial_investment_entry.get())
    cash_flows = [float(x.strip()) for x in cash_flows_entry.get().split(",")]
    discount_rate = float(discount_rate_entry.get())
    pi = calculate_pi(initial_investment, cash_flows, discount_rate)
    pi_label.config(text="Profitability Index: " + str(round(pi, 2)))

calculate_button = tk.Button(root, text="Calculate", command=calculate_pi_callback)

# Arrange the widgets using the grid layout manager
initial_investment_label.grid(row=0, column=0)
initial_investment_entry.grid(row=0, column=1)
cash_flows_label.grid(row=1, column=0)
cash_flows_entry.grid(row=1, column=1)
discount_rate_label.grid(row=2, column=0)
discount_rate_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)
pi_label.grid(row=4, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()
