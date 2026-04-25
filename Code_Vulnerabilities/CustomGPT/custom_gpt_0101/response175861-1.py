
import pandas as pd
import matplotlib.pyplot as plt

# Read stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window
fixed_window_start = 1000  # Starting index for fixed window
fixed_window_end = fixed_window_start + 30

# Extract the fixed window for IBM
fixed_ibm_window = IBM.iloc[fixed_window_start:fixed_window_end]

# Initialize an empty list to store rolling correlations
correlations = []

# Calculate correlations with every 30-day window in GE
for start in range(len(GE) - 30 + 1):
    ge_window = GE.iloc[start:start + 30]
    correlation = fixed_ibm_window.corr(ge_window)
    correlations.append(correlation)

# Convert correlations to a DataFrame for easier plotting
correlation_series = pd.Series(correlations, index=range(len(correlations)))

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation of Fixed IBM Window with GE')
plt.xlabel('Starting Day of GE Window')
plt.ylabel('Correlation')
plt.show()
