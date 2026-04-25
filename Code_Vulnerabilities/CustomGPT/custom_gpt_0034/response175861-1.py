
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window (for example: days 1001-1030)
start_index = 1000  # 0-based index for day 1001
end_index = start_index + 30
fixed_window_IBM = IBM[start_index:end_index]

# Calculate rolling correlation
rolling_corrs = []
for i in range(len(GE) - 30 + 1):
    rolling_window_GE = GE[i:i + 30]
    corr = fixed_window_IBM.corr(rolling_window_GE)
    rolling_corrs.append(corr)

# Adjusting for the index
dates = GE.index[30 - 1:]  # Aligning dates to start from the first complete window
rolling_corr_series = pd.Series(rolling_corrs, index=dates)

# Plotting
plt.plot(rolling_corr_series)
plt.title("Rolling Correlation of Fixed IBM Window with GE")
plt.xlabel("Date")
plt.ylabel("Correlation Coefficient")
plt.show()
