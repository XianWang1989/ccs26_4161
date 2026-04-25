
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window
fixed_start = 1000  # Starting index for the fixed window (e.g., day 1001)
fixed_end = fixed_start + 30  # Fixed window of 30 days
fixed_window_ibm = IBM[fixed_start:fixed_end]

# Storage for correlation results
correlations = []

# Calculate correlations for every possible 30-day window in GE
for start in range(len(GE) - 29):  # Ensuring we can fit a 30-day window
    rolling_window_ge = GE[start:start + 30]
    corr = np.corrcoef(fixed_window_ibm, rolling_window_ge)[0, 1]
    correlations.append(corr)

# Convert correlations to a Series for easy plotting
correlation_series = pd.Series(correlations, index=GE.index[0:len(correlations)])

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation Between Fixed IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
