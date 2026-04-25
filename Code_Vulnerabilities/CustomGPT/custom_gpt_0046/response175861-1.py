
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window (for example, rows 1001 to 1030)
fixed_window = GE.iloc[1000:1030]

# Calculate rolling correlation with the fixed window
rolling_corr = IBM.rolling(window=30).corr(fixed_window)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(rolling_corr, label='Rolling Correlation with GE (Fixed Window)')
plt.title('Rolling Correlation of IBM with Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
