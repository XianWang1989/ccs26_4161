
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select the stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the window size
window = 30

# Calculate rolling correlation for each 30-day window of IBM with the fixed window of GE
fixed_ge_window = GE[1000:1030]  # Adjust based on your specific index needs
roll_cor = []
for i in range(len(IBM) - window + 1):
    temp_window = IBM[i:i + window]
    correlation = fixed_ge_window.corr(temp_window)
    roll_cor.append(correlation)

# Create a Series for the rolling correlation results
roll_cor_series = pd.Series(roll_cor, index=IBM.index[window - 1:])

# Plot the results
plt.plot(roll_cor_series)
plt.title('Rolling Correlation between IBM and GE (fixed GE window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
