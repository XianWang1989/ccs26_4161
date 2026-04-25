
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE
start_ge = 1000  # starting index for GE (e.g., day 1001)
window_size = 30  # 30-day window

# Extract the constant window for GE
ge_window = GE[start_ge:start_ge + window_size]

# Prepare to store correlations
correlations = []

# Loop through IBM to calculate correlation with the GE window
for start_ibm in range(len(IBM) - window_size + 1):
    ibm_window = IBM[start_ibm:start_ibm + window_size]
    correlation = ge_window.corr(ibm_window)
    correlations.append(correlation)

# Create a new DataFrame with the results
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the rolling correlations
plt.plot(correlation_series)
plt.xlabel('Date')
plt.ylabel('Correlation with GE (Days 1001-1030)')
plt.title('Rolling Correlation of IBM with GE (Constant 30-Day Window)')
plt.show()
