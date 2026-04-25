
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (e.g., days 1001-1030)
fixed_start = 1000  # Start index for GE (1001 in 1-based indexing)
fixed_end = fixed_start + 30  # End index for 30-day window for GE
fixed_ge_window = GE.iloc[fixed_start:fixed_end]

# Calculate rolling correlation of IBM with the fixed GE window
roll_cor = []
for i in range(len(IBM) - 30 + 1):
    current_window = IBM.iloc[i:i + 30]
    correlation = current_window.corr(fixed_ge_window)
    roll_cor.append(correlation)

# Convert to a Series for easy plotting
roll_cor_series = pd.Series(roll_cor, index=IBM.index[:len(roll_cor)])

# Plot the rolling correlation
plt.plot(roll_cor_series)
plt.title('Rolling Correlation of IBM to Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
