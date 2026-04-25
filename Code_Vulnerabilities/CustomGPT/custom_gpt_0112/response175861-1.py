
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Extract IBM and GE stock prices
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the window length
window = 30

# Hold the constant window for IBM (e.g., days 1001-1030)
fixed_window_start = 1000  # Adjust as needed, Python uses 0-based indexing
fixed_window = IBM.iloc[fixed_window_start:fixed_window_start + window]

# Calculate rolling correlation with the fixed window against all 30-day windows of GE
correlations = []
for start in range(len(GE) - window + 1):
    current_window = GE.iloc[start:start + window]
    correlation = fixed_window.corr(current_window)
    correlations.append(correlation)

# Convert the list to a DataFrame for easier handling
rolling_cor = pd.Series(correlations, index=GE.index[window - 1:])

# Plot the results
plt.figure(figsize=(14, 7))
plt.plot(rolling_cor, label='Rolling Correlation with IBM Fixed Window')
plt.title('Rolling Correlation of GE against IBM Fixed Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
