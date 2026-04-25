
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (e.g., days 1001-1030)
fixed_window_start = 1000  # index for day 1001
fixed_window_end = 1030     # index for day 1030
GE_fixed_window = GE.iloc[fixed_window_start:fixed_window_end]

# Calculate rolling correlation
roll_cor = []
for i in range(len(IBM) - len(GE_fixed_window) + 1):
    IBM_window = IBM.iloc[i:i + len(GE_fixed_window)]
    correlation = GE_fixed_window.corr(IBM_window)
    roll_cor.append(correlation)

# Convert the rolling correlation list to a pandas Series
roll_cor_series = pd.Series(roll_cor, index=IBM.index[0:len(roll_cor)])

# Plot the rolling correlation
plt.plot(roll_cor_series)
plt.title('Rolling Correlation between GE (fixed window) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
