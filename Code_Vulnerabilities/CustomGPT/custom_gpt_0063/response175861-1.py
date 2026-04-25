
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock price data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window (e.g., days 1001-1030 for GE)
constant_start = 1000  # Adjust for zero-based indexing
constant_end = constant_start + 30

# Extract the constant window for GE
constant_window_GE = GE[constant_start:constant_end]

# Initialize an empty list to hold the correlations
correlations = []

# Calculate the correlation for each 30-day window of IBM
for start in range(len(IBM) - 30 + 1):
    window_IBM = IBM[start:start + 30]
    correlation = constant_window_GE.corr(window_IBM)
    correlations.append(correlation)

# Create a Series for the correlations
correlation_series = pd.Series(correlations, index=IBM.index[0:len(correlations)])

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE (Constant Window) with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
