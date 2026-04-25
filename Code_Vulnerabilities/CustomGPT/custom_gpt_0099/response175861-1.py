
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Select a constant window for GE (for example, days 1001-1030)
fixed_start = 1000  # Replace with the actual index start (zero-based)
fixed_window = GE.iloc[fixed_start:fixed_start + 30]

# Initialize a list to store correlations
correlations = []

# Calculate the correlation for every possible 30-day window in IBM
for start in range(len(IBM) - 29):  # Subtract 29 to prevent out-of-bounds
    rolling_window = IBM.iloc[start:start + 30]
    correlation = rolling_window.corr(fixed_window)  # Compute correlation
    correlations.append(correlation)

# Convert correlations to a DataFrame for easier plotting
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the rolling correlations
plt.plot(correlation_series)
plt.title('Correlation of Fixed GE Window with Rolling IBM Windows')
plt.ylabel('Correlation')
plt.xlabel('Date')
plt.show()
