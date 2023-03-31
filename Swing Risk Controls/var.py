# SWING TRADING RISK CONTROLS LEVEL ONE.

# TASK LIST

# GOAL = WRAP GUI - SCREEN 1.
# LINK TO stock_data.csv as TRANSFORMABLE by FUNCTIONS BELOW.

# -	VALUE AT RISK Formula – Maximum Expected Loss / Level of Confidence.
# -	Expected Shortfall (E.S.) Formula – measure of the expected loss given that VaR has been exceeded.
# -	Correlation: a measure of the relationship between two securities or assets, typically represented by a number between -1 and 1.
# -	Omega Ratio: Measure of risk-adjusted return
# -	Sartino Ratio: accounts for downside deviation of portfolio.


# Add & Improve Corresponding Graphs

# Prepare code to transfer between 'Stock Analysis' & 'Portfolio (Bundled Stocks) Aseembly

# IMPORTATION OF MODULES
import tkinter as tk
from tkinter import messagebox
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import quad

# GENERATES DESIRED returns SEQUENCE for VAR SCRIPT ...
# IDEALLY WOULD LIKE TO OPEN AND HABITUALLY UPDATE stock_data.CSV as to MONITOR & MANAGE TRADES.

# Create a DataFrame containing the stock data
df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
                   'Stock1': [100, 101, 102, 103, 104],
                   'Stock2': [105, 103, 104, 106, 108]})

# Write the DataFrame to a CSV file
df.to_csv('stock_data.csv', index=False)

# Load the data for the two stocks into a DataFrame
df = pd.read_csv('stock_data.csv')


# SWING TRADING RISK CONTROLS LEVEL I. TECHNOLOGIES

# CALCULATING THE VAR - AN ESSENTIAL  INDICATOR FOR EXITING & ENTERING.

def var_calculator(returns, confidence_level):
    # Mean and standard deviation of returns
    mean = np.mean(returns)
    stddev = np.std(returns)

    # Calculate the significance level (alpha)
    alpha = 1 - confidence_level

    # Calculate VaR
    var = norm.ppf(alpha, mean, stddev)

    return var


# EXPECTED SHORTFALL ( WIP )

# Calculate expected loss in the worst scenario.

# GOAL IS TO LINK EXPECTED SHORTFALL TO GUI & WRITABLE TO  stock_data.CSV



# OMEGA RATIO - MEASURES RISK-ADJUSTED-RETURN





# SARTINO RATIO accounts for downside deviation of portfolio.




# THE GRAPH & GUI

# Function to calculate correlation
def calculate_correlation():
    correlation = df['stock1'].corr(df['stock2'])
    messagebox.showinfo("Correlation", f"The correlation between stock1 and stock2 is {correlation:.2f}")


def calculate():
    try:
        # get the input values
        conf_level = float(confidence_level_var.get())
        returns = list(map(float, returns_array.get().split(",")))
        var = var_calculator(returns, conf_level)
        var_value_label.config(text=f"VAR: {var:.2f}")

        # create the graph
        fig, ax = plt.subplots()
        ax.plot(returns, label='Returns')
        ax.axhline(var, color='red', label='VaR')
        ax.set_title('Returns vs VaR')
        ax.set_xlabel('Returns')
        ax.set_ylabel('VaR')
        ax.legend()
        plt.show()

        # Call the correlation calculation function
        calculate_correlation()

    except ValueError:
        messagebox.showerror("Error", "Invalid input value")


root = tk.Tk()
root.title("Value at Risk Calculator")

# Confidence Level input
confidence_level_label = tk.Label(root, text="Confidence level:")
confidence_level_label.grid(row=0, column=0, sticky="W")
confidence_level_var = tk.StringVar()
confidence_level_entry = tk.Entry(root, textvariable=confidence_level_var)
confidence_level_entry.grid(row=0, column=1)

# Alpha input
alpha_label = tk.Label(root, text="Alpha:")
alpha_label.grid(row=3, column=0, sticky="W")
alpha_var = tk.StringVar()
alpha_entry = tk.Entry(root, textvariable=alpha_var)
alpha_entry.grid(row=3, column=1)

# returns input
returns_label = tk.Label(root, text="Returns array(comma separated):")
returns_label.grid(row=1, column=0, sticky="W")
returns_array = tk.StringVar()
returns_entry = tk.Entry(root, textvariable=returns_array)
returns_entry.grid(row=1, column=1)

# VAR value label
var_value_label = tk.Label(root, text="VAR:")
var_value_label.grid(row=2, column=0, columnspan=2)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
