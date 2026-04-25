
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Define the stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Select the fixed window for IBM (e.g., days 1001-1030)
fixed_start = 1000  # Adjust based on your DataFrame index
fixed_end = 1030
fixed_window_ibm = IBM.iloc[fixed_start:fixed_end]

# Prepare to store rolling correlations
rolling_correlations = []

# Calculate correlation with the fixed window against all possible windows in GE
for start in range(len(GE) - 30 + 1):
    end = start + 30
    window_ge = GE.iloc[start:end]

    correlation = fixed_window_ibm.corr(window_ge)
    rolling_correlations.append(correlation)

# Convert results to a Series
result_series = pd.Series(rolling_correlations, index=GE.index[30-1:])

# Plot the results
plt.plot(result_series)
plt.title('Rolling Correlation of Fixed IBM Window with GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
