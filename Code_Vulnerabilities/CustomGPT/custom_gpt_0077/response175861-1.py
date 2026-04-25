
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE
constant_window = GE[1000:1030]  # Days 1001 to 1030 (index 1000 to 1029)

# Prepare a list to store correlation results
correlations = []

# Calculate rolling correlations
for start in range(len(IBM) - 30):
    rolling_window = IBM[start:start + 30]
    corr = constant_window.corr(rolling_window)
    correlations.append(corr)

# Convert correlations to a DataFrame for better handling
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation between GE (Days 1001-1030) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axhline(0, color='black', lw=0.5, ls='--')  # Optional: Add a horizontal line at y=0
plt.show()
