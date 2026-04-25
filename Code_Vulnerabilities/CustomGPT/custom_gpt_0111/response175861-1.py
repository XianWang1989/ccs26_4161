
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window start and end dates
constant_start = 1000  # Starting index for the constant window
constant_end = constant_start + 30

# Get the slice for the constant window
constant_window_IBM = IBM.iloc[constant_start:constant_end]

# Initialize a list to store correlations
correlations = []

# Loop through every possible 30-day window in GE
for start in range(len(GE) - 30):
    window_GE = GE.iloc[start:start + 30]

    # Compute the correlation and append to the list
    correlation = constant_window_IBM.corr(window_GE)
    correlations.append(correlation)

# Convert the list of correlations to a DataFrame
correlation_series = pd.Series(correlations, index=GE.index[30:])

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(correlation_series)
plt.title('Rolling Correlation of Constant IBM Window with GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid()
plt.show()
