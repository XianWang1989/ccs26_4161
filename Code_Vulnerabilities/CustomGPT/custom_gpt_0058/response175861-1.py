
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the constant window for GE (e.g., days 1001-1030)
start_day = 1000  # Using 0-based index for Python
constant_window = GE[start_day:start_day + 30]

# Prepare a list to store the correlation results
correlations = []

# Iterate through all possible 30-day windows in IBM
for i in range(len(IBM) - 30 + 1):
    current_window = IBM[i:i + 30]
    # Calculate the correlation with the constant GE window
    corr = constant_window.corr(current_window)
    correlations.append(corr)

# Convert the results into a Series for plotting
correlations_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the rolling correlations
plt.figure(figsize=(12, 6))
plt.plot(correlations_series)
plt.title('Rolling Correlation of IBM with Constant 30-Day GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid()
plt.show()
