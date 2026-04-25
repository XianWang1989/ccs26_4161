
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for IBM
fixed_window = IBM[1000:1030]  # Use data from day 1001 to 1030 (0-indexed)

# Initialize a list to hold correlation results
correlations = []

# Iterate over possible rolling windows of GE
for start in range(len(GE) - len(fixed_window) + 1):
    current_window = GE[start:start + len(fixed_window)]
    correlation = fixed_window.corr(current_window)
    correlations.append(correlation)

# Convert to a DataFrame for easier plotting
correlation_series = pd.Series(correlations, index=GE.index[:len(correlations)])

# Plot the result
plt.figure(figsize=(10, 5))
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE with Fixed IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
