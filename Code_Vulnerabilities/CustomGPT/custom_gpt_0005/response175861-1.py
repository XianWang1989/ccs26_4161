
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
fixed_window_start = 1001
fixed_window_end = fixed_window_start + 30
fixed_GE = GE.iloc[fixed_window_start:fixed_window_end]

# Calculate rolling correlation of IBM with fixed GE window
rolling_cor = [
    fixed_GE.corr(IBM.iloc[i:i + 30]) for i in range(len(IBM) - 30 + 1)
]

# Create a new DataFrame for the correlation results
rolling_cor_df = pd.DataFrame(rolling_cor, index=IBM.index[:len(rolling_cor)], columns=['Correlation'])

# Plot the results
plt.plot(rolling_cor_df)
plt.title('Rolling Correlation of IBM with Fixed GE Window')
plt.ylabel('Correlation')
plt.xlabel('Date')
plt.show()
