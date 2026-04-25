
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select IBM and GE stock prices
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the starting index for the constant window
start_index = 1000  # Example: 1001st day in zero-based index
constant_window = IBM[start_index:start_index + 30]

correlations = []
windows = []

# Iterate over GE stock prices to create rolling windows of 30 days
for i in range(len(GE) - 30 + 1):
    current_window = GE[i:i + 30]
    correlation = constant_window.corr(current_window)
    correlations.append(correlation)
    windows.append(IBM.index[i])

# Create a DataFrame to hold the results
results = pd.DataFrame({'Date': windows, 'Correlation': correlations})
results.set_index('Date', inplace=True)

# Plot the correlations
plt.figure(figsize=(10, 5))
plt.plot(results.index, results['Correlation'])
plt.title('Correlation between 30-day IBM Window and Rolling GE Windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axhline(0, color='grey', linestyle='--')
plt.show()
