
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the starting point for the constant window
start_point = 1001  # Adjust this index based on the DataFrame
constant_window = GE[start_point:start_point + 30]

# Prepare an empty list to store correlation values
correlations = []

# Calculate correlations with every 30-day window in IBM
for i in range(len(IBM) - 30):
    current_window = IBM[i:i + 30]
    correlation = constant_window.corr(current_window)
    correlations.append(correlation)

# Convert correlations list to a Series for easier plotting
correlation_series = pd.Series(correlations, index=IBM.index[30:])

# Plot the correlations
plt.plot(correlation_series)
plt.title('Correlation between constant GE window and rolling IBM windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
