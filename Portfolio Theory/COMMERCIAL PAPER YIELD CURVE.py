import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

class CommercialPaperYieldCurve(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Commercial Paper Yield Curve Analysis")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create input labels and fields
        tk.Label(self, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Maturity (days):").grid(row=1, column=0, padx=5, pady=5)
        self.maturity_entry = tk.Entry(self)
        self.maturity_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Rate (%):").grid(row=2, column=0, padx=5, pady=5)
        self.rate_entry = tk.Entry(self)
        self.rate_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Create plot button
        self.plot_button = tk.Button(self, text="Plot Yield Curve", command=self.plot_curve)
        self.plot_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Initialize data frame
        self.cp_data = pd.DataFrame(columns=['Date', 'Maturity', 'Rate'])

    def submit_data(self):
        # Get input values
        date = self.date_entry.get()
        maturity = int(self.maturity_entry.get())
        rate = float(self.rate_entry.get())

        # Append values to data frame
        self.cp_data = self.cp_data.append({'Date': date, 'Maturity': maturity, 'Rate': rate}, ignore_index=True)

        # Clear input fields
        self.date_entry.delete(0, tk.END)
        self.maturity_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)

        # Show success message
        messagebox.showinfo("Success", "Data submitted successfully.")

    def plot_curve(self):
        if len(self.cp_data) == 0:
            messagebox.showwarning("Error", "No data to plot.")
            return

        # Convert date column to datetime format
        self.cp_data['Date'] = pd.to_datetime(self.cp_data['Date'])

        # Set Date column as index
        self.cp_data.set_index('Date', inplace=True)

        # Calculate yields based on 360-day year
        self.cp_data['Yield'] = (360 / self.cp_data['Maturity']) * self.cp_data['Rate']

        # Pivot the table to get yields by maturity
        yield_data = self.cp_data.pivot(columns='Maturity', values='Yield')

        # Plot the yield curve
        yield_data.plot()

        # Add labels and title
        plt.xlabel('Maturity')
        plt.ylabel('Yield')
        plt.title
