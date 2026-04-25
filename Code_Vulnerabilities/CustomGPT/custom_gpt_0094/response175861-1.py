
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the constant window for GE (e.g., days 1001-1030)
constant_window_start = 1000  # Adjust as necessary
constant_window_end = constant_window_start + 30

# Extract the constant window for GE
constant_GE = GE.iloc[constant_window_start:constant_window_end]

# Prepare to store correlation results
correlations = []

# Iterate through all possible 30-day windows of IBM
for start in range(len(IBM) - 29):
    IBM_window = IBM.iloc[start:start + 30]
    correlation = constant_GE.corr(IBM_window)
    correlations.append(correlation)

# Create a series for correlations with appropriate index
correlation_series = pd.Series(correlations, index=range(len(correlations)))

# Plot the correlation series
plt.plot(correlation_series)
plt.title('Correlation of Constant GE Window with Rolling IBM Windows')
plt.xlabel('IBM Window Start Index')
plt.ylabel('Correlation')
plt.show()
