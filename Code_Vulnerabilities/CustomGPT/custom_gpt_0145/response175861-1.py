
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices from the CSV file
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Fix the window for GE (e.g., days 1001-1030)
fixed_window_start = 1000  # Adjust this index based on your actual DataFrame
fixed_window_end = fixed_window_start + 30

# Extract the fixed window for GE
fixed_GE_window = GE.iloc[fixed_window_start:fixed_window_end]

# Calculate rolling correlation for each possible 30-day window in IBM with fixed GE window
correlations = []
for start in range(len(IBM) - 30 + 1):
    current_window = IBM.iloc[start:start + 30]
    correlation = current_window.corr(fixed_GE_window)
    correlations.append(correlation)

# Convert to a Series for easier plotting
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation: IBM vs. Fixed GE Window (Days 1001-1030)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid()
plt.show()
