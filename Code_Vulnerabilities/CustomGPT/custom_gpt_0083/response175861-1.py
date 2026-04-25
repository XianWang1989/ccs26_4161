
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window start and end
fixed_start = 1001
fixed_end = 1031

# Extract the fixed window for IBM
ibm_fixed_window = IBM[fixed_start:fixed_end]

# Prepare to store rolling correlations
rolling_correlations = []

# Calculate rolling correlation against fixed IBM window
for start in range(len(GE) - (fixed_end - fixed_start) + 1):
    ge_window = GE[start:start + (fixed_end - fixed_start)]
    correlation = ibm_fixed_window.corr(ge_window)
    rolling_correlations.append(correlation)

# Create a DataFrame for the results
results = pd.DataFrame(rolling_correlations, index=GE.index[fixed_start:len(GE) - (fixed_end - fixed_start) + 1], columns=['Correlation'])

# Plot the results
plt.plot(results)
plt.title('Rolling Correlation between Fixed IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
