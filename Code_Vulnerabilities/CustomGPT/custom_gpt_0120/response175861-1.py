
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
fixed_window_start = 1000  # starting index for the fixed window
fixed_window_end = fixed_window_start + 30

# Extract the fixed window data for GE
fixed_ge = GE.iloc[fixed_window_start:fixed_window_end]

# List to hold correlation results
correlations = []

# Calculate correlation for every 30-day window in IBM
for start in range(len(IBM) - 29):  # Adjust range to fit rolling windows
    rolling_ibm = IBM.iloc[start:start + 30]
    correlation = fixed_ge.corr(rolling_ibm)
    correlations.append(correlation)

# Convert to a Series for easy plotting
correlation_series = pd.Series(correlations, index=IBM.index[:-29])

# Plot the rolling correlations
plt.figure(figsize=(12, 6))
plt.plot(correlation_series, label='Fixed GE vs Rolling IBM Correlation')
plt.title('Correlation between Fixed GE Window and Rolling IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
