
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for GE (e.g., days 1001-1030)
fixed_window_start = 1000  # Start at index 1001 (0-based index)
fixed_window_end = 1030    # End at index 1030 (0-based index)
fixed_GE = GE.iloc[fixed_window_start:fixed_window_end]

# Prepare to store correlations
correlations = []

# Calculate rolling correlation for each 30-day window in IBM against the fixed GE window
for i in range(len(IBM) - 30 + 1):
    rolling_window = IBM.iloc[i:i + 30]
    corr = rolling_window.corr(fixed_GE)
    correlations.append(corr)

# Convert correlations list to a DataFrame for plotting
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the rolling correlations
plt.figure(figsize=(12, 6))
plt.plot(correlation_series)
plt.title('Rolling Correlation of IBM with Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
