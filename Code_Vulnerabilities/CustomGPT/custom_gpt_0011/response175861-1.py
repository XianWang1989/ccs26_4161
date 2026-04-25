
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the stock prices from a CSV file
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM (for example, days 1001-1030)
fixed_start_date = '2020-01-01'  # Example start date; adjust as necessary
fixed_end_date = '2020-01-30'    # Example end date; adjust as necessary

# Extract the fixed window for IBM
fixed_ibm_window = IBM[(IBM.index >= fixed_start_date) & (IBM.index <= fixed_end_date)]

# Prepare to hold the correlations
correlations = []

# Slide 30-day window across GE stock prices
window_size = 30
for i in range(len(GE) - window_size + 1):
    ge_window = GE[i:i + window_size]
    correlation = fixed_ibm_window.corr(ge_window)
    correlations.append(correlation)

# Create a date index for the rolling correlations
correlation_dates = GE.index[:len(correlations)]
rolling_corr = pd.Series(correlations, index=correlation_dates)

# Plot the rolling correlations
plt.plot(rolling_corr)
plt.title('Rolling Correlation between IBM (Fixed Window) and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
