
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window
fixed_start = 1000  # starting index for the fixed window
fixed_end = fixed_start + 30  # ending index for the fixed window
fixed_window_ibm = IBM.iloc[fixed_start:fixed_end]

# Prepare a storage for correlations
correlations = []

# Loop through possible windows in GE
for i in range(len(GE) - 30 + 1):
    # Slice the GE stock for the current window
    window_ge = GE.iloc[i:i + 30]
    # Calculate the correlation with the fixed window of IBM
    correlation = fixed_window_ibm.corr(window_ge)
    correlations.append(correlation)

# Create a DataFrame to hold the rolling correlations
rolling_correlations = pd.Series(correlations, index=GE.index[0:len(correlations)])

# Plot the results
plt.plot(rolling_correlations)
plt.title('Rolling Correlation between Fixed IBM Window and GE Windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
