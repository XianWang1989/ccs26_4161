
import pandas as pd
import matplotlib.pyplot as plt

# Load your data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE
constant_window_start = 1000  # Adjust to your actual index for days
constant_window_end = constant_window_start + 30
constant_ge_window = GE[constant_window_start:constant_window_end]

# Prepare a list to hold correlations
correlations = []

# Iterate through each possible 30-day window in IBM
for start in range(len(IBM) - 30 + 1):
    ibm_window = IBM[start:start + 30]
    correlation = ibm_window.corr(constant_ge_window)
    correlations.append(correlation)

# Convert correlations to a Series for easier plotting
correlation_series = pd.Series(correlations, index=range(len(correlations)))

# Plot the results
plt.plot(correlation_series)
plt.title('Correlation of IBM with Constant GE Window')
plt.xlabel('IBM 30-Day Window Start Index')
plt.ylabel('Correlation with GE (Fixed Window)')
plt.show()
