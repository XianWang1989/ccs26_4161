
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your stock price data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window (adjusting for zero-indexing)
fixed_start = 1001
fixed_end = fixed_start + 30
fixed_ge_window = GE.iloc[fixed_start:fixed_end]

# Create an empty list to store correlation results
correlations = []

# Calculate rolling correlation
for start in range(len(IBM) - 30):
    current_ibm_window = IBM.iloc[start:start + 30]
    correlation = current_ibm_window.corr(fixed_ge_window)
    correlations.append(correlation)

# Convert to a Series for plotting
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(correlation_series)
plt.title('Rolling Correlation between IBM and GE (Fixed GE Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axvline(x=IBM.index[fixed_start], color='red', linestyle='--', label='Fixed Window Start')
plt.axvline(x=IBM.index[fixed_end - 1], color='red', linestyle='--', label='Fixed Window End')
plt.legend()
plt.show()
