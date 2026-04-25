
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window (e.g., days 1001-1030)
fixed_start = 1000  # using 0-based indexing
fixed_end = fixed_start + 30
fixed_window = IBM.iloc[fixed_start:fixed_end]

# Prepare to store correlations
correlations = []

# Iterate through possible windows in GE
for start in range(len(GE) - 30 + 1):
    rolling_window = GE.iloc[start:start + 30]
    correlation = fixed_window.corr(rolling_window).iloc[0, 0]
    correlations.append(correlation)

# Create a DataFrame for the correlations
correlation_series = pd.Series(correlations, index=range(len(GE) - 30 + 1))

# Plot the correlations
plt.figure(figsize=(10, 5))
plt.plot(correlation_series)
plt.title('Correlation of IBM (Days 1001-1030) with Rolling 30-Day Windows of GE')
plt.xlabel('GE Rolling Window Start Index')
plt.ylabel('Correlation')
plt.grid()
plt.show()
