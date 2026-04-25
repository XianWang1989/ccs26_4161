
import pandas as pd
import matplotlib.pyplot as plt

# Read stock prices from a CSV file
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the constant window range for GE (e.g., days 1001-1030)
start_date = '1001-01-01'  # adjust to your actual date format
end_date = '1001-01-30'
GE_window = GE[start_date:end_date]

# Create a list to hold correlations
correlations = []

# Calculate rolling correlation
for start in range(len(IBM) - 29):  # Loop through IBM's prices
    end = start + 30
    IBM_window = IBM[start:end]
    corr = GE_window.corr(IBM_window)
    correlations.append(corr)

# Create a date index for the correlations
dates = IBM.index[29:]  # Drop the first 29 dates for alignment
correlation_series = pd.Series(correlations, index=dates)

# Plot the correlations
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE with Constant IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
