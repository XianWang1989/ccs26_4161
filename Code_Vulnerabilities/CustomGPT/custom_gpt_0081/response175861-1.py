
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select the individual stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the window size
window_size = 30

# Specify the constant window indices for IBM (using days 1001-1030 as an example)
start_day = 1000  # 0-based index
constant_IBM_window = IBM.iloc[start_day:start_day + window_size]

# Create a list to hold the correlation values
correlations = []

# Iterate through each possible window in GE
for i in range(len(GE) - window_size + 1):
    rolling_GE_window = GE.iloc[i:i + window_size]
    correlation = constant_IBM_window.corr(rolling_GE_window)
    correlations.append(correlation)

# Create a new DataFrame to store the rolling correlation results
correlation_series = pd.Series(correlations, index=GE.index[window_size - 1:])

# Plot the correlation series
plt.figure(figsize=(14, 7))
plt.plot(correlation_series, label='Rolling Correlation of GE with IBM (30-day fixed window)')
plt.title('Rolling Correlation between GE and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.grid()
plt.show()
