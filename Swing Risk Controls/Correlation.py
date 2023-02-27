import pandas as pd

# Load the data for the two stocks into a DataFrame
df = pd.read_csv('stock_data.csv')

# Calculate the Pearson correlation coefficient
correlation = df['stock1'].corr(df['stock2'])

print(correlation)