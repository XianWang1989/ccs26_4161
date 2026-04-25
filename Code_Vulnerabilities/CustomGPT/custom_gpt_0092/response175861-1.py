
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have already read your data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the start and end indices for the constant window
start_idx = 1000  # Day 1001 in zero-indexing
end_idx = start_idx + 30

# Extract the constant window for IBM
constant_window = IBM.iloc[start_idx:end_idx]

# Initialize a list to store correlations
correlations = []

# Loop through GE with a rolling window of 30 days
for i in range(len(GE) - 30 + 1):
    rolling_window = GE[i:i + 30]
    corr = constant_window.corr(rolling_window)
    correlations.append(corr)

# Create a DataFrame to hold the results
correlation_series = pd.Series(correlations, index=GE.index[:len(correlations)])

# Plot the rolling correlations
plt.plot(correlation_series)
plt.title('Correlation between GE (rolling) and IBM (constant window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
