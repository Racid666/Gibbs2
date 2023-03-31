import yfinance as yf
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def perform_linear_regression(ticker, index):
    # Define the stock symbol and time period
    start_date = '2023-01-01'
    end_date = '2023-03-10'

    # Download the stock data using yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Drop any missing values from the DataFrame
    stock_data.dropna(inplace=True)

    # Download the market index data using yfinance
    index_data = yf.download(index, start=start_date, end=end_date)

    # Drop any missing values from the DataFrame
    index_data.dropna(inplace=True)

    # Merge the stock and index data into a single DataFrame
    data = pd.concat([stock_data['Close'], index_data['Close']], axis=1)
    data.columns = ['Stock Price', 'Market Index']

    # Set independent and dependent variables
    X = data[['Market Index']]
    y = data['Stock Price']

    # Create linear regression object and fit the model
    reg = LinearRegression().fit(X, y)

    # Print intercept and coefficient values
    print('Intercept:', reg.intercept_)
    print('Coefficients:', reg.coef_)

    # Make predictions
    y_pred = reg.predict(X)

    # Plot actual vs predicted values
    plt.scatter(y, y_pred)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Linear Regression for ' + ticker + ' with ' + index)
    plt.show()

def on_click():
    ticker = entry_ticker.get()
    index = entry_index.get()
    perform_linear_regression(ticker, index)

# Create GUI
root = tk.Tk()
root.title('Stock Linear Regression')
label_ticker = tk.Label(root, text='Enter Ticker Symbol:')
entry_ticker = tk.Entry(root)
label_index = tk.Label(root, text='Enter Market Index:')
entry_index = tk.Entry(root)
button = tk.Button(root, text='Perform Linear Regression', command=on_click)
label_ticker.pack()
entry_ticker.pack()
label_index.pack()
entry_index.pack()
button.pack()
root.mainloop()


print('Intercept:', reg.intercept_)
