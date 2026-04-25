
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window start and end
fixed_start = 1000  # Change as needed
fixed_end = fixed_start + 30

# Get the fixed window data
fixed_GE = GE.iloc[fixed_start:fixed_end]

# Initialize an empty list to store correlation values
correlations = []

# Calculate correlations for each 30-day window of IBM
for start in range(len(IBM) - 30):
    current_window = IBM.iloc[start:start + 30]
    corr = current_window.corr(fixed_GE)
    correlations.append(corr)

# Create a correlation series with an appropriate index
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation of Fixed GE Window with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
