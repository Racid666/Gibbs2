import yfinance as yf
import pandas as pd
import tkinter as tk

# Define function to download stock data
def download_data():
    # Get input values from GUI
    ticker = entry_ticker.get()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()

    # Download data from Yahoo Finance
    data = yf.download(ticker, start=start_date, end=end_date)

    # Save data to CSV file
    data.to_csv('stock_data.csv')

    # Print message
    print('Stock data downloaded and saved to stock_data.csv')

# Create GUI
root = tk.Tk()
root.title('Stock Data Downloader')

# Create input fields
label_ticker = tk.Label(root, text='Ticker:')
label_ticker.grid(row=0, column=0, padx=5, pady=5)
entry_ticker = tk.Entry(root)
entry_ticker.grid(row=0, column=1, padx=5, pady=5)

label_start_date = tk.Label(root, text='Start date (YYYY-MM-DD):')
label_start_date.grid(row=1, column=0, padx=5, pady=5)
entry_start_date = tk.Entry(root)
entry_start_date.grid(row=1, column=1, padx=5, pady=5)

label_end_date = tk.Label(root, text='End date (YYYY-MM-DD):')
label_end_date.grid(row=2, column=0, padx=5, pady=5)
entry_end_date = tk.Entry(root)
entry_end_date.grid(row=2, column=1, padx=5, pady=5)

# Set default values
entry_ticker.insert(0, 'AAPL')
entry_start_date.insert(0, '2021-01-01')
entry_end_date.insert(0, '2021-12-31')

# Create download button
button_download = tk.Button(root, text='Download', command=download_data)
button_download.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

root.mainloop()
