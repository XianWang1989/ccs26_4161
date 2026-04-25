
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window index for GE (for example, days 1001-1030)
start_index = 1000  # Adjust based on your actual index
end_index = start_index + 30
GE_window = GE.iloc[start_index:end_index]

# Prepare a list to hold correlation results
correlations = []

# Calculate correlation for each 30-day window in IBM
for i in range(len(IBM) - 29):  # Adjust for window size
    IBM_window = IBM.iloc[i:i + 30]
    corr = GE_window.corr(IBM_window)
    correlations.append(corr)

# Create a new Series for the correlations
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the correlations
plt.plot(correlation_series)
plt.title('Rolling Correlation with Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
