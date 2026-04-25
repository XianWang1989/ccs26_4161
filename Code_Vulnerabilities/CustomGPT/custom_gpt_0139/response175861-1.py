
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select specific stock series
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (example: days 1001 to 1030)
fixed_window_start = 1000  # Replace with the actual index based on your data
fixed_window_end = fixed_window_start + 30
fixed_GE = GE.iloc[fixed_window_start:fixed_window_end]

# Prepare to hold correlation results
rolling_corrs = []

# Loop through IBM to compute the correlation with the fixed GE window
for start in range(len(IBM) - 30 + 1):
    end = start + 30
    rolling_IBM = IBM.iloc[start:end]

    # Calculate correlation
    correlation = fixed_GE.corr(rolling_IBM)
    rolling_corrs.append(correlation)

# Create an index for the rolling correlations
corr_index = IBM.index[:len(rolling_corrs)]

# Plot the rolling correlations
plt.figure(figsize=(10, 5))
plt.plot(corr_index, rolling_corrs, label='Rolling Correlation with Fixed GE Window')
plt.title('Rolling Correlation Between GE (Fixed Window) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
