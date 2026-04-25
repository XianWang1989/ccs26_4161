
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the index for the fixed window (e.g., days 1001-1030)
start_index = 1000  # Adjust based on zero-indexing
fixed_window = IBM[start_index:start_index + 30]  # Fixed window for IBM
fixed_window GE_prices = GE.rolling(window=30)  # Rolling window for GE

# Calculate correlation
correlations = []
for i in range(len(GE) - 30):
    current_window = GE[i:i + 30]
    corr = fixed_window.corr(current_window)
    correlations.append(corr)

# Create a DateTime index for plotting
correlation_indices = GE.index[30:]  # Aligning indices for the correlation results

# Plot the correlations
plt.plot(correlation_indices, correlations)
plt.title("Fixed 30-day Correlation of IBM with GE Rolling Windows")
plt.xlabel("Date")
plt.ylabel("Correlation")
plt.show()
