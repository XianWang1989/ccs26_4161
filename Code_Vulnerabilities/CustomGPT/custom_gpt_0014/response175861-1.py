
import pandas as pd
import matplotlib.pyplot as plt

# Load data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM (e.g., days 1001-1030)
fixed_start = 1000  # Change to actual index for your data
fixed_end = fixed_start + 30

# Fixed window series for IBM
fixed_ibm = IBM.iloc[fixed_start:fixed_end]

# List to hold correlations
correlations = []

# Loop through GE to calculate correlations
for start in range(len(GE) - 30 + 1):
    rolling_ge = GE.iloc[start:start + 30]
    corr = fixed_ibm.corr(rolling_ge)
    correlations.append(corr)

# Create a DataFrame for the correlation results
correlation_series = pd.Series(correlations, index=GE.index[:len(correlations)])

# Plot the rolling correlations
plt.figure(figsize=(10, 5))
plt.plot(correlation_series)
plt.title('Rolling Correlation between IBM (fixed window) and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axvline(x=GE.index[fixed_start], color='r', linestyle='--', label='Fixed Window Start')
plt.axvline(x=GE.index[fixed_end-1], color='r', linestyle='--', label='Fixed Window End')
plt.legend()
plt.show()
