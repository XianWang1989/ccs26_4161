
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define fixed window
start_day = 1000  # Assuming 0-based index, so this is for the days 1001-1030
fixed_window = IBM[start_day:start_day + 30]

# Initialize a list to store correlations
correlations = []

# Calculate rolling correlation with fixed 30 days of IBM and all possible windows of GE
for i in range(len(GE) - 29):  # Loop through GE prices
    rolling_window = GE.iloc[i:i + 30]  # 30-day window for GE
    correlation = fixed_window.corr(rolling_window)
    correlations.append(correlation)

# Convert to DataFrame for easier plotting
correlation_series = pd.Series(correlations, index=GE.index[:len(correlations)])

# Plot the correlation
plt.figure(figsize=(12,6))
plt.plot(correlation_series)
plt.title('Rolling Correlation between Fixed 30 Days of IBM and 30 Days of GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid()
plt.show()
