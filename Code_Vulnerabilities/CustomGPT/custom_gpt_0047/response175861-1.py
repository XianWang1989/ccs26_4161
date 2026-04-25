
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE (for example, days 1001-1030)
start_date = 'Date_of_1001'  # replace with actual date
end_date = 'Date_of_1030'  # replace with actual date
constant_ge_window = GE.loc[start_date:end_date]

# Calculate rolling correlations
correlations = []
for start in range(len(IBM) - 29):  # Loop through every possible 30-day window in IBM
    ibm_window = IBM.iloc[start:start + 30]
    corr = constant_ge_window.corr(ibm_window)
    correlations.append(corr)

# Create a DataFrame for the correlations
correlation_series = pd.Series(correlations, index=IBM.index[:-29])  # Align index

# Plotting the correlation
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE (fixed window) with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
