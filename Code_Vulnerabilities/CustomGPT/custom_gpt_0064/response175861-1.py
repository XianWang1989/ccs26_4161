
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for IBM (e.g., days 1001-1030)
fixed_start = 1000  # Adjust based on actual index
fixed_end = fixed_start + 30
fixed_ibm_window = IBM.iloc[fixed_start:fixed_end]

# Prepare to store rolling correlations
correlations = []

# Calculate rolling correlations of GE with the fixed IBM window
for start in range(len(GE) - 30 + 1):
    ge_window = GE.iloc[start:start + 30]
    correlation = fixed_ibm_window.corr(ge_window)  # Calculate the correlation
    correlations.append(correlation)

# Create a DataFrame for the correlation results
correlation_series = pd.Series(correlations, index=GE.index[:len(correlations)])

# Plot the rolling correlations
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE with Fixed IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid()
plt.show()
