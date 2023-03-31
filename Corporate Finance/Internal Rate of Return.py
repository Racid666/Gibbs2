import tkinter as tk
import numpy as np

# Define the IRR function
def calculate_irr(cash_flows):
    return np.irr(cash_flows)

# Define the GUI
root = tk.Tk()
root.title("IRR Calculator")

# Define the input fields
cash_flows_label = tk.Label(root, text="Cash Flows (comma-separated):")
cash_flows_entry = tk.Entry(root)

# Define the output field
irr_label = tk.Label(root, text="IRR: 0%")

# Define the calculate button
def calculate_irr_callback():
    cash_flows = [float(x.strip()) for x in cash_flows_entry.get().split(",")]
    irr = calculate_irr(cash_flows) * 100
    irr_label.config(text="IRR: " + str(round(irr, 2)) + "%")

calculate_button = tk.Button(root, text="Calculate", command=calculate_irr_callback)

# Arrange the widgets using the grid layout manager
cash_flows_label.grid(row=0, column=0)
cash_flows_entry.grid(row=0, column=1)
calculate_button.grid(row=1, column=0, columnspan=2)
irr_label.grid(row=2, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()
