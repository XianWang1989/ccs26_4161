
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Fixed 30-day window for IBM (e.g., days 1001-1030)
fixed_window_start = 1000  # index position for day 1001
fixed_window_end = fixed_window_start + 30  # position for day 1030

fixed_ibm_window = IBM.iloc[fixed_window_start:fixed_window_end]

# Compute rolling correlation with GE
rolling_cor = GE.rolling(window=30).corr(fixed_ibm_window)

# Plotting the results
plt.plot(rolling_cor, label='Rolling Correlation with Fixed IBM Window')
plt.title('Rolling Correlation of GE with Fixed IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
