import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

# Define function to run simulation
def run_simulation():
    # Get input values from GUI
    initial_investment = int(entry_initial_investment.get())
    years = int(entry_years.get())
    annual_returns_mean = float(entry_returns_mean.get())
    annual_returns_std = float(entry_returns_std.get())
    trials = int(entry_trials.get())

    # Generate random samples of annual returns
    annual_returns = np.random.normal(annual_returns_mean, annual_returns_std, trials)

    # Calculate compound annual growth rate for each trial
    cagr = (1 + annual_returns) ** years - 1

    # Calculate final portfolio value for each trial
    final_value = initial_investment * (1 + cagr)

    # Calculate statistics of final portfolio values
    mean_final_value = np.mean(final_value)
    std_final_value = np.std(final_value)
    min_final_value = np.min(final_value)
    max_final_value = np.max(final_value)

    # Plot distribution of final portfolio values
    plt.hist(final_value, bins=50)
    plt.xlabel('Final Portfolio Value')
    plt.ylabel('Frequency')
    plt.title('Monte Carlo Simulation for Stock Trading')
    plt.show()

    # Print summary statistics
    label_output_mean.config(text='Mean final portfolio value: $' + str(round(mean_final_value, 2)))
    label_output_std.config(text='Standard deviation of final portfolio value: $' + str(round(std_final_value, 2)))
    label_output_min.config(text='Minimum final portfolio value: $' + str(round(min_final_value, 2)))
    label_output_max.config(text='Maximum final portfolio value: $' + str(round(max_final_value, 2)))


# Create GUI
root = tk.Tk()
root.title('Monte Carlo Simulation for Stock Trading')

# Create input fields
label_initial_investment = tk.Label(root, text='Initial investment:')
label_initial_investment.grid(row=0, column=0, padx=5, pady=5)
entry_initial_investment = tk.Entry(root)
entry_initial_investment.grid(row=0, column=1, padx=5, pady=5)

label_years = tk.Label(root, text='Number of years:')
label_years.grid(row=1, column=0, padx=5, pady=5)
entry_years = tk.Entry(root)
entry_years.grid(row=1, column=1, padx=5, pady=5)

label_returns_mean = tk.Label(root, text='Mean annual returns:')
label_returns_mean.grid(row=2, column=0, padx=5, pady=5)
entry_returns_mean = tk.Entry(root)
entry_returns_mean.grid(row=2, column=1, padx=5, pady=5)

label_returns_std = tk.Label(root, text='Standard deviation of annual returns:')
label_returns_std.grid(row=3, column=0, padx=5, pady=5)
entry_returns_std = tk.Entry(root)
entry_returns_std.grid(row=3, column=1, padx=5, pady=5)

label_trials = tk.Label(root, text='Number of trials:')
label_trials.grid(row=4, column=0, padx=5, pady=5)
entry_trials = tk.Entry(root)
entry_trials.grid(row=4, column=1, padx=5, pady=5)

button_run = tk.Button(root, text='Run Simulation', command=run_simulation)
button_run.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

label_output_mean = tk.Label(root, text='Mean final portfolio value:')
label_output_mean.grid(row=6, column=0, padx=5, pady=5)
label_output_std = tk.Label(root, text='Standard deviation of final portfolio value:')
label_output_std.grid(row=7, column=0, padx=5, pady=5)
label_output_min = tk.Label(root, text='Minimum final portfolio value:')
label_output_min.grid(row=8, column=0, padx=5, pady=5)
label_output_max = tk.Label(root, text='Maximum final portfolio value:')
label_output_max.grid(row=9, column=0, padx=5, pady=5)


label_output_mean_value = tk.Label(root, text='')
label_output_mean_value.grid(row=6, column=1, padx=5, pady=5)
label_output_std_value = tk.Label(root, text='')
label_output_std_value.grid(row=7, column=1, padx=5, pady=5)
label_output_min_value = tk.Label(root, text='')
label_output_min_value.grid(row=8, column=1, padx=5, pady=5)
label_output_max_value = tk.Label(root, text='')
label_output_max_value.grid(row=9, column=1, padx=5, pady=5)


entry_initial_investment.insert(0, '10000')
entry_years.insert(0, '10')
entry_returns_mean.insert(0, '0.08')
entry_returns_std.insert(0, '0.15')
entry_trials.insert(0, '1000')


root.mainloop()
