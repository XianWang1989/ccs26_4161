
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window range for IBM
start_index = 1000  # Adjust based on your specific DataFrame index
fixed_window = IBM[start_index:start_index + 30]

# Prepare to collect the correlations
correlations = []

# Calculate rolling correlations with the fixed window for GE
for i in range(len(GE) - 29):  # Ensure there's a full 30-day window
    rolling_window = GE[i:i + 30]
    correlation = fixed_window.corr(rolling_window)
    correlations.append(correlation)

# Create a Series for the correlation results
correlation_series = pd.Series(correlations, index=GE.index[:len(correlations)])

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE with Fixed Window of IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
