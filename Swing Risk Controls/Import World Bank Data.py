import pandas as pd
import wbdata

def export_data():
    # Define indicators and countries to download
    indicators = {'NY.GDP.MKTP.CD': 'GDP', 'FP.CPI.TOTL.ZG': 'Inflation'}
    countries = ['US', 'CA', 'MX']

    # Download data from World Bank API
    data = wbdata.get_dataframe(indicators, country=countries, convert_date=True)

    # Rename columns
    data.columns = ['GDP', 'Inflation']

    # Reset index and convert date to a column
    data = data.reset_index()

    # Export GDP and inflation data to CSV files
    data[['date', 'GDP']].to_csv('gdp_data.csv', index=False)
    data[['date', 'Inflation']].to_csv('inflation_data.csv', index=False)

    # Print message
    print('GDP data exported to gdp_data.csv')
    print('Inflation data exported to inflation_data.csv')

# Call function to export data
export_data()
