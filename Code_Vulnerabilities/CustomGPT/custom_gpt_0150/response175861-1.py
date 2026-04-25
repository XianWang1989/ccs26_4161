
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for GE (days 1001 to 1030)
fixed_ge_window = GE.iloc[1000:1030]  # Adjusting for zero-based index

# Prepare to store correlations
correlations = []

# Loop through all possible 30-day windows in IBM
for start in range(len(IBM) - 29):
    ibm_window = IBM.iloc[start:start + 30]
    correlation = fixed_ge_window.corr(ibm_window)
    correlations.append(correlation)

# Convert correlations to a Series with appropriate index
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the correlation results
plt.plot(correlation_series)
plt.title('Correlation between GE and Moving 30-day Windows of IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
