
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for IBM
start_index = 1000  # Adjust based on your DataFrame's index
end_index = start_index + 30  # 30-day window

# Get the constant window data for IBM
IBM_window = IBM[start_index:end_index]

# Prepare to store the rolling correlations
corrs = []

# Calculate correlations for all 30-day windows in GE
for i in range(len(GE) - 30 + 1):
    GE_window = GE[i:i + 30]
    correlation = IBM_window.corr(GE_window)
    corrs.append(correlation)

# Create a DataFrame to hold results with the corresponding dates
date_range = GE.index[:len(corrs)]
correlation_series = pd.Series(corrs, index=date_range)

# Plot the rolling correlations
plt.plot(correlation_series)
plt.title('Rolling Correlation between IBM Constant Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
