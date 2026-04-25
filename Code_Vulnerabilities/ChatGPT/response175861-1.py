
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming your StockPrices.csv file is already prepared with appropriate date and stock data
StockPrices = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Define the window size
window_size = 30

# Define the start day for holding GE constant
start_day = 1001  # Adjust this as needed for your dataset
end_day = start_day + window_size - 1

# Extract the price series for IBM and GE
IBM = StockPrices['IBM']
GE = StockPrices['GE']

# Select the constant window of GE stock prices
constant_GE_window = GE[start_day:end_day]

# Create an array to hold the rolling correlation values
rolling_corr_values = []

# Calculate the rolling correlation
for start_idx in range(len(IBM) - window_size + 1):
    # Get the current window of IBM stock prices
    current_IBM_window = IBM.iloc[start_idx:start_idx + window_size]
    # Calculate the correlation with the constant GE window
    correlation = current_IBM_window.corr(constant_GE_window)
    rolling_corr_values.append(correlation)

# Create a new index for the rolling correlation results
rolling_corr_index = IBM.index[:len(rolling_corr_values)]

# Convert the list into a pandas Series
rolling_corr_series = pd.Series(rolling_corr_values, index=rolling_corr_index)

# Plotting the rolling correlation
plt.plot(rolling_corr_series)
plt.title('Rolling Correlation of IBM with Constant GE Window (Days 1001-1030)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
