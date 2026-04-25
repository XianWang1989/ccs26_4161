import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM'].reset_index(drop=True)
GE = Stocks['GE'].reset_index(drop=True)

# Define the fixed 30-day window from GE (e.g., days 1000–1029 for 0-based indexing)
ge_fixed_window = GE[1000:1030].values

# Ensure window size
window_size = 30
correlations = []

# Slide through IBM to get rolling 30-day windows and correlate with fixed GE window
for i in range(len(IBM) - window_size + 1):
    ibm_window = IBM[i:i + window_size].values
    if len(ibm_window) == len(ge_fixed_window):
        corr = np.corrcoef(ibm_window, ge_fixed_window)[0, 1]
        correlations.append(corr)
    else:
        correlations.append(np.nan)

# Plot the rolling correlation
plt.plot(correlations)
plt.title("Rolling Correlation with GE Window (Days 1001-1030)")
plt.xlabel("Start Day of IBM Window")
plt.ylabel("Correlation")
plt.show()
