
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
start_index = 1000  # Adjust this for the desired starting point
fixed_window = GE[start_index:start_index + 30]

# Prepare to store correlations
correlations = []

# Calculate correlation for each possible 30-day window in IBM
for i in range(len(IBM) - 30):
    current_window = IBM[i:i + 30]
    corr = fixed_window.corr(current_window)
    correlations.append(corr)

# Create a Series for correlations with the correct index
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the results
plt.figure(figsize=(14, 7))
plt.plot(correlation_series, label='Rolling Correlation with GE (Fixed Window)')
plt.title('Rolling Correlation between IBM and Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
