
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window start and length
constant_start = 1001  # Starting index for GE's window
window_length = 30

# Extract the constant window for GE
ge_window = GE[constant_start:constant_start + window_length]

# Create a list to store correlation values
correlations = []

# Calculate correlations with the constant GE window
for start in range(len(IBM) - window_length + 1):
    ibm_window = IBM[start:start + window_length]
    correlation = ibm_window.corr(ge_window)
    correlations.append(correlation)

# Create a series for the correlations with appropriate index
correlation_series = pd.Series(correlations, index=range(len(correlations)))

# Plot the correlations
plt.plot(correlation_series)
plt.title('Rolling Correlation: Constant GE Window vs. IBM')
plt.xlabel('Start Index for IBM')
plt.ylabel('Correlation')
plt.show()
