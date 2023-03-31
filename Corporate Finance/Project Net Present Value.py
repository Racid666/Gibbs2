import tkinter as tk

# Define the NPV function
def calculate_npv(initial_investment, cash_flows, discount_rate, time_scale):
    if time_scale == "Monthly":
        periods = 12
    elif time_scale == "Weekly":
        periods = 52
    else:
        periods = 1
    discounted_cash_flows = [cash_flow / ((1 + discount_rate / periods) ** n) for n, cash_flow in enumerate(cash_flows)]
    npv = sum(discounted_cash_flows) - initial_investment
    return npv

# Define the GUI
root = tk.Tk()
root.title("NPV Calculator")

# Define the input fields
initial_investment_label = tk.Label(root, text="Initial Investment:")
initial_investment_entry = tk.Entry(root)
cash_flows_label = tk.Label(root, text="Cash Flows (comma-separated):")
cash_flows_entry = tk.Entry(root)
discount_rate_label = tk.Label(root, text="Discount Rate:")
discount_rate_entry = tk.Entry(root)
time_scale_label = tk.Label(root, text="Time Scale:")
time_scale = tk.StringVar()
time_scale.set("Monthly")
time_scale_dropdown = tk.OptionMenu(root, time_scale, "Monthly", "Weekly", "Yearly")

# Define the output field
npv_label = tk.Label(root, text="NPV: $0")

# Define the calculate button
def calculate_npv_callback():
    initial_investment = float(initial_investment_entry.get())
    cash_flows = [float(x.strip()) for x in cash_flows_entry.get().split(",")]
    discount_rate = float(discount_rate_entry.get())
    time_scale_val = time_scale.get()
    npv = calculate_npv(initial_investment, cash_flows, discount_rate, time_scale_val)
    npv_label.config(text="NPV: $" + str(round(npv, 2)))

calculate_button = tk.Button(root, text="Calculate", command=calculate_npv_callback)

# Arrange the widgets using the grid layout manager
initial_investment_label.grid(row=0, column=0)
initial_investment_entry.grid(row=0, column=1)
cash_flows_label.grid(row=1, column=0)
cash_flows_entry.grid(row=1, column=1)
discount_rate_label.grid(row=2, column=0)
discount_rate_entry.grid(row=2, column=1)
time_scale_label.grid(row=3, column=0)
time_scale_dropdown.grid(row=3, column=1)
calculate_button.grid(row=4, column=0, columnspan=2)
npv_label.grid(row=5, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()
