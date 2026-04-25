
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

window_length = 30
fixed_window_start = 1000
fixed_window_end = fixed_window_start + window_length

fixed_ge_window = GE[fixed_window_start:fixed_window_end]

rolling_correlations = []
for start in range(len(IBM) - window_length + 1):
    current_ibm_window = IBM[start:start + window_length]
    correlation = fixed_ge_window.corr(current_ibm_window)
    rolling_correlations.append(correlation)

plt.plot(rolling_correlations)
plt.title('Rolling Correlation between Fixed GE Window and IBM')
plt.xlabel('Starting Day of IBM Window')
plt.ylabel('Correlation')
plt.show()
