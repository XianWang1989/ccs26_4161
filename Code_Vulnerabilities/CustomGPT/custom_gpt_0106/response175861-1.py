
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Specify the range for GE
start = 1000
end = 1030

# Extract the constant window for GE
GE_constant = GE[start:end]

# Initialize a list to store the rolling correlations
rolling_corrs = []

# Calculate rolling correlation
for i in range(len(IBM) - len(GE_constant) + 1):
    window_IBM = IBM[i:i + len(GE_constant)]
    correlation = GE_constant.corr(window_IBM)
    rolling_corrs.append(correlation)

# Create a Series for the rolling correlations
rolling_corr_series = pd.Series(rolling_corrs, index=IBM.index[:len(rolling_corrs)])

# Plot the results
plt.plot(rolling_corr_series)
plt.title('Rolling Correlation between GE (Days 1001-1030) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid()
plt.show()
