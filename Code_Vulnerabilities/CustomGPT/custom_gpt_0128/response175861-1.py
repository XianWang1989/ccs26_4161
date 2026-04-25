
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
fixed_window_start = 1000
fixed_window_end = fixed_window_start + 30

# Extract the fixed window for GE
ge_window = GE[fixed_window_start:fixed_window_end]

# List to hold correlation values
correlations = []

# Iterate over IBM to correlate with the fixed GE window
for start in range(len(IBM) - 30):  # Adjusted range to ensure 30-day window
    ibm_window = IBM[start:start + 30]
    correlation = ge_window.corr(ibm_window)
    correlations.append(correlation)

# Create a correlation series indexed by IBM's starting days
correlation_series = pd.Series(correlations, index=range(len(correlations)))

# Plot the correlation
plt.plot(correlation_series)
plt.title('Rolling Correlation with Fixed GE Window (Days 1001-1030)')
plt.xlabel('Starting Day of IBM Window')
plt.ylabel('Correlation')
plt.show()
