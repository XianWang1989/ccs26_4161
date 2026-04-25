
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Fixed window: days 1001 to 1030 (adjust index as necessary)
fixed_window_start = 1000  # Adjust based on your actual index
fixed_window_end = 1030

# Extract the fixed window for IBM
fixed_window_IBM = IBM.iloc[fixed_window_start:fixed_window_end]

# Prepare an empty list to store correlations
correlations = []

# Iterate over all possible 30-day windows for GE
for start in range(len(GE) - 30 + 1):
    end = start + 30
    window_GE = GE.iloc[start:end]
    correlation = fixed_window_IBM.corr(window_GE)
    correlations.append(correlation)

# Convert to a DataFrame for easy plotting
correlation_series = pd.Series(correlations, index=range(len(correlations)))

# Plot the correlations
plt.plot(correlation_series)
plt.title('Rolling Correlation with Fixed Window (IBM 1001-1030 vs GE)')
plt.xlabel('Starting Day of GE Window')
plt.ylabel('Correlation')
plt.show()
