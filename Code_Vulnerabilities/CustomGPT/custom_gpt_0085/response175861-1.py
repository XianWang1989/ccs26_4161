
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define window size
window_size = 30
# Constant window for IBM (days 1001-1030)
ibm_window = IBM[1000:1030]  # Adjust indexing if necessary

# Storage for rolling correlations
correlations = []

# Iterate over possible starting points for GE
for start in range(len(GE) - window_size + 1):
    ge_window = GE[start:start + window_size]
    corr = ibm_window.corr(ge_window)
    correlations.append(corr)

# Convert to DataFrame for easier plotting
correlation_dates = GE.index[:len(correlations)]
corr_df = pd.DataFrame(correlations, index=correlation_dates, columns=['Correlation'])

# Plot the correlations
plt.figure(figsize=(12, 6))
plt.plot(corr_df.index, corr_df['Correlation'], label='Rolling Correlation', color='blue')
plt.title('Rolling Correlation Between Constant IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
