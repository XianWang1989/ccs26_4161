
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (e.g., days 1001-1030)
fixed_start = 1000  # Replace with your actual index (zero-based)
fixed_end = 1030
fixed_window_GE = GE.iloc[fixed_start:fixed_end]

# Function to calculate rolling correlation
def rolling_fixed_corr(fixed_window, series, window_size):
    correlations = []
    for start in range(len(series) - window_size + 1):
        end = start + window_size
        rolling_window = series.iloc[start:end]
        corr = fixed_window.corr(rolling_window)
        correlations.append(corr)
    return np.array(correlations)

# Calculate the correlations
roll_cor = rolling_fixed_corr(fixed_window_GE, IBM, window_size=30)

# Create a date range for the correlations
correlation_dates = IBM.index[0:len(roll_cor)]  # Adjust index based on correlation length

# Plot the results
plt.plot(correlation_dates, roll_cor, label='Correlation with GE (fixed window)')
plt.title('Rolling Correlation between IBM and Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axvline(x=IBM.index[fixed_start], color='red', linestyle='--', label='Fixed Window Start')
plt.axvline(x=IBM.index[fixed_end-1], color='red', linestyle='--', label='Fixed Window End')
plt.legend()
plt.show()
