import tkinter as tk
from yahoo_fin import stock_info as si

import yfinance as yf


def get_stock_data(ticker):
    stock_info = yf.Ticker(ticker).info
    return {
        'regularMarketPrice': stock_info.get('regularMarketPrice'),
        'trailingEps': stock_info.get('trailingEps'),
        'bookValue': stock_info.get('bookValue'),
        'dividendsPerShare': stock_info.get('dividendsPerShare'),
        'netIncomeToCommon': stock_info.get('netIncomeToCommon'),
        'sharesOutstanding': stock_info.get('sharesOutstanding'),
        'totalStockholderEquity': stock_info.get('totalStockholderEquity'),
        'totalDebt': stock_info.get('totalDebt'),
    }
    return stock_data


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





def fetch_data():
    ticker = e_ticker.get()
    try:
        stock_data = get_stock_data(ticker)
    except Exception as e:
        result_label.config(text=f"Error fetching data: {e}")
        return

    e1.delete(0, tk.END)
    e1.insert(0, stock_data['regularMarketPrice'])

    e2.delete(0, tk.END)
    e2.insert(0, stock_data['trailingEps'])

    e3.delete(0, tk.END)
    e3.insert(0, stock_data['bookValue'])

    e4.delete(0, tk.END)
    e4.insert(0, stock_data['dividendsPerShare'])

    e5.delete(0, tk.END)
    e5.insert(0, stock_data['netIncomeToCommon'])

    e6.delete(0, tk.END)
    e6.insert(0, stock_data['sharesOutstanding'])

    e7.delete(0, tk.END)
    e7.insert(0, stock_data['totalStockholderEquity'])

    e8.delete(0, tk.END)
    e8.insert(0, stock_data['totalDebt'])

    result_label.config(text="")


def calculate():
    try:
        stock_price = float(e1.get())
        eps_input = float(e2.get())
        book_value_per_share = float(e3.get())
        annual_dividend_payment = float(e4.get())
        net_income = float(e5.get())
        shares_outstanding = float(e6.get())
        shareholder_equity = float(e7.get())
        total_debt = float(e8.get())
    except ValueError:
        result_label.config(text="Error: Please make sure all input fields are filled with valid numbers.")
        return

    results = "Results:\n"
    results += f"P/E Ratio: {pe_ratio(stock_price, eps_input):.2f}\n"
    results += f"P/B Ratio: {pb_ratio(stock_price, book_value_per_share):.2f}\n"
    results += f"Dividend Yield: {dividend_yield(annual_dividend_payment, stock_price) * 100:.2f}%\n"
    results += f"EPS: {eps(net_income, shares_outstanding):.2f}\n"
    results += f"ROE: {roe(net_income, shareholder_equity) * 100:.2f}%\n"
    results += f"Debt-to-Equity Ratio: {debt_to_equity(total_debt, shareholder_equity):.2f}"

    result_label.config(text=results)


root = tk.Tk()

tk.Label(root, text="Stock Ticker").grid(row=0, column=0)
e_ticker = tk.Entry(root)
e_ticker.grid(row=0, column=1)

fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.grid(row=0, column=2)


labels = [
    "Stock Price",
    "EPS",
    "Book Value per Share",
    "Annual Dividend Payment",
    "Net Income",
    "Shares Outstanding",
    "Shareholder Equity",
    "Total Debt",
]

for idx, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=idx + 1)

entry_vars = [tk.StringVar() for _ in range(len(labels))]
entries = [tk.Entry(root, textvariable=var) for var in entry_vars]

for idx, entry in enumerate(entries):
    entry.grid(row=idx + 1, column=1)

e1, e2, e3, e4, e5, e6, e7, e8 = entry_vars

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=9, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=10, columnspan=2)

root.mainloop()
