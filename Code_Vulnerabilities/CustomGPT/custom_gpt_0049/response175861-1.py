
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select the stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the constant window for IBM starting from a specific index, for example, from date[1000] to date[1030]
start_index = 1000  # Adjust based on your DataFrame index
constant_window = IBM[start_index:start_index + 30]

# Prepare to store correlation results
correlations = []

# Iterate over all possible 30-day windows in GE
for i in range(len(GE) - 30 + 1):
    rolling_window = GE[i:i + 30]
    correlation = constant_window.corr(rolling_window)
    correlations.append(correlation)

# Convert correlations to a Pandas Series for easier plotting
correlation_series = pd.Series(correlations, index=GE.index[start_index:len(GE) - 30 + 1])

# Plotting the results
plt.plot(correlation_series)
plt.title('Rolling Correlation of Constant IBM Window with GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axhline(0, color='gray', linestyle='--', lw=1)  # Add a horizontal line at y=0
plt.show()
