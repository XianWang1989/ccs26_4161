
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices into a DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select the stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Fixed window for GE (days 1001-1030)
fixed_window_start = 1000  # Change as needed (0-indexed)
fixed_window_end = fixed_window_start + 30

# Extract the fixed window for GE
ge_fixed_window = GE.iloc[fixed_window_start:fixed_window_end]

# Prepare to store correlation results
correlations = []

# Iterate through all possible 30-day windows in IBM
for i in range(len(IBM) - 30 + 1):
    ibm_window = IBM.iloc[i:i + 30]
    correlation = ibm_window.corr(ge_fixed_window)
    correlations.append(correlation)

# Create a Series for correlation results
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the rolling correlation
plt.plot(correlation_series)
plt.title('Correlation of IBM with GE (Fixed Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
