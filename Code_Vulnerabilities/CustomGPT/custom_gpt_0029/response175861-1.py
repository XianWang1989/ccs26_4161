
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
fixed_start = 1000  # Start index (0-based) for GE
fixed_end = 1030    # End index (0-based) for GE
ge_fixed_window = GE.iloc[fixed_start:fixed_end]

# Prepare to collect correlations
correlations = []

# Loop through all possible 30-day windows in IBM
for start in range(len(IBM) - 30 + 1):
    ibm_window = IBM.iloc[start:start + 30]
    correlation = ge_fixed_window.corr(ibm_window)  # Calculate correlation
    correlations.append(correlation)

# Create a Series for correlations
correlation_series = pd.Series(correlations, index=range(len(correlations)))

# Plot the results
plt.plot(correlation_series)
plt.title('Correlation of GE (Days 1001-1030) with Rolling IBM Windows')
plt.xlabel('Starting Day for IBM Window')
plt.ylabel('Correlation')
plt.show()
