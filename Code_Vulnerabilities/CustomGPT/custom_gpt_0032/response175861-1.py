
import pandas as pd
import matplotlib.pyplot as plt

# Read the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE (e.g., days 1001-1030)
start_index = 1000  # 0-based index for day 1001
end_index = start_index + 30

# Select the constant window for GE
constant_window_GE = GE.iloc[start_index:end_index]

# Prepare to store correlations
correlations = []

# Calculate rolling correlation for each 30-day window of IBM
for i in range(len(IBM) - 30 + 1):
    rolling_window_IBM = IBM.iloc[i:i + 30]
    correlation = rolling_window_IBM.corr(constant_window_GE)
    correlations.append(correlation)

# Convert correlations to a DataFrame
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation of IBM with Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
