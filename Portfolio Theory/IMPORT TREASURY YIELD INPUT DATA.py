from fredapi import Fred
import pandas as pd

# API key for FRED
fred = Fred(api_key='YOUR_API_KEY')

# Download data for 10-year treasury bond yield, 3-month treasury bill yield, and S&P 500 index earnings yield
data = fred.get_series(['DGS10', 'DGS3MO', 'SP500EarningsYield'])

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=['Yield'])

# Print the values of each yield
print('10-year treasury bond yield:', round(df.loc['DGS10']['Yield'], 2), '%')
print('3-month treasury bill yield:', round(df.loc['DGS3MO']['Yield'], 2), '%')
print('S&P 500 index earnings yield:', round(df.loc['SP500EarningsYield']['Yield'], 2), '%')
