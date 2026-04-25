
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Choose a fixed window for GE (e.g., from days 1001 to 1030)
start_index = 1000  #0-based index, so this corresponds to day 1001
fixed_window = GE.iloc[start_index:start_index + 30]

# Calculate rolling correlations
correlations = []
for i in range(len(IBM) - 30 + 1):  # Adjust for rolling window
    rolling_window = IBM.iloc[i:i + 30]
    correlation = fixed_window.corr(rolling_window)
    correlations.append(correlation)

# Convert to a DataFrame for easier plotting
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the correlations
plt.figure(figsize=(10, 5))
plt.plot(correlation_series)
plt.title('Rolling Correlation (Fixed GE window vs IBM)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
