import tkinter as tk

# Define functions for the formulas
def pe_ratio(stock_price, eps):
    return stock_price / eps

def pb_ratio(stock_price, book_value_per_share):
    return stock_price / book_value_per_share

def dividend_yield(annual_dividend_payment, stock_price):
    return annual_dividend_payment / stock_price

def eps(net_income, shares_outstanding):
    return net_income / shares_outstanding

def roe(net_income, shareholder_equity):
    return net_income / shareholder_equity

def debt_to_equity(total_debt, shareholder_equity):
    return total_debt / shareholder_equity

# Create a GUI with entry fields for the input values
root = tk.Tk()

tk.Label(root, text="Stock Price").grid(row=0)
tk.Label(root, text="EPS").grid(row=1)
tk.Label(root, text="Book Value per Share").grid(row=2)
tk.Label(root, text="Annual Dividend Payment").grid(row=3)
tk.Label(root, text="Net Income").grid(row=4)
tk.Label(root, text="Shares Outstanding").grid(row=5)
tk.Label(root, text="Shareholder Equity").grid(row=6)
tk.Label(root, text="Total Debt").grid(row=7)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e4 = tk.Entry(root)
e5 = tk.Entry(root)
e6 = tk.Entry(root)
e7 = tk.Entry(root)
e8 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)

# Define a function to calculate the formulas when the button is clicked
def calculate():
    stock_price = float(e1.get())
    eps = float(e2.get())
    book_value_per_share = float(e3.get())
    annual_dividend_payment = float(e4.get())
    net_income = float(e5.get())
    shares_outstanding = float(e6.get())
    shareholder_equity = float(e7.get())
    total_debt = float(e8.get())

    results = "Results:\n"
    results += "P/E Ratio: {:.2f}\n".format(pe_ratio(stock_price, eps))
    results += "P/B Ratio: {:.2f}\n".format(pb_ratio(stock_price, book_value_per_share))
    results += "Dividend Yield: {:.2f}%\n".format(dividend_yield(annual_dividend_payment, stock_price) * 100)
    results += "EPS: {:.2f}\n".format(eps(net_income, shares_outstanding))
    results += "ROE: {:.2f}%\n".format(roe(net_income, shareholder_equity) * 100)
    results += "Debt-to-Equity Ratio: {:.2f}".format(debt_to_equity(total_debt, shareholder_equity))

    result_label.config(text=results)

# Create a button to calculate the formulas
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=8, columnspan=2)

# Create a label to display the results
result_label = tk.Label(root, text="")
result_label.grid(row=9, columnspan=2)

# Run the GUI
root.mainloop()
