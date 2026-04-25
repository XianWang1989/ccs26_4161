
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for GE (days 1001-1030)
ge_window = GE[1000:1030]  # Adjust index as necessary

# Prepare a list to store correlations
correlations = []

# Calculate correlation with sliding window of IBM
for start in range(len(IBM) - 29):  # Adjust to ensure full 30-day windows
    ibm_window = IBM[start:start + 30]
    corr = ge_window.corr(ibm_window)
    correlations.append(corr)

# Create a Series for plotting
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the correlation series
plt.figure(figsize=(12, 6))
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE (Fixed Window) with IBM (Sliding Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
