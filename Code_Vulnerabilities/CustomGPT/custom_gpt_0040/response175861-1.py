
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window (e.g., from index 1001 to 1030)
fixed_start = 1000  # Python uses 0-based indexing
fixed_end = 1030

# Extract the fixed window for IBM
fixed_window_IBM = IBM.iloc[fixed_start:fixed_end]

# Calculate rolling correlation with the fixed window against GE
rolling_cor = GE.rolling(window=30).corr(fixed_window_IBM)

# Plot the rolling correlation
plt.figure(figsize=(12, 6))
plt.plot(rolling_cor, label='Rolling Correlation with Fixed IBM Window', color='blue')
plt.title('Rolling Correlation of GE with Fixed 30-Day IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
