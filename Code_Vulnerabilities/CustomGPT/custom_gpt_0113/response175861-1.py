
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM (days 1001-1030)
fixed_window_start = 1000  # Adjust according to your DataFrame index
fixed_window_end = 1030
fixed_IBM_window = IBM.iloc[fixed_window_start:fixed_window_end]

# Calculate rolling correlations
rolling_correlations = []
for start in range(len(GE) - 30 + 1):
    window_GE = GE.iloc[start:start + 30]
    correlation = fixed_IBM_window.corr(window_GE).iloc[0, 0]
    rolling_correlations.append(correlation)

# Create a Series for the results
rolling_cor_series = pd.Series(rolling_correlations, index=GE.index[30-1:])

# Plot the results
plt.plot(rolling_cor_series)
plt.title('Rolling Correlation of IBM (fixed window) with GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
