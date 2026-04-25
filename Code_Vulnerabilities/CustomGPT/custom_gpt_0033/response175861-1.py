
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed and sliding window sizes
fixed_window_size = 30
sliding_window_size = 30

# Create a function to calculate correlations
def fixed_window_corr(IBM_series, GE_series, fixed_start, window_size):
    # Extract the fixed window
    fixed_window = IBM_series[fixed_start:fixed_start + window_size]

    # Store the correlation results
    correlations = []

    # Loop over the sliding window
    for start in range(len(GE_series) - window_size + 1):
        sliding_window = GE_series[start:start + window_size]
        correlation = fixed_window.corr(sliding_window)
        correlations.append(correlation)

    return pd.Series(correlations, index=GE_series.index[:len(correlations)])

# Set the fixed starting point
fixed_start = '1001-01-01'  # Adjust the date as appropriate
results = fixed_window_corr(IBM, GE, fixed_start, fixed_window_size)

# Plot the results
plt.plot(results)
plt.title('Correlation between Fixed IBM Window and Sliding GE Windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
