
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window start and end
fixed_start = 1000  # Adjust according to your DataFrame's index
fixed_end = fixed_start + 30

# Extract the fixed window data for IBM
fixed_window_ibm = IBM.iloc[fixed_start:fixed_end]

# Prepare to store rolling correlations
rolling_correlations = []

# Iterate over GE to calculate correlation with the fixed window
for i in range(len(GE) - 30 + 1):
    rolling_window_ge = GE.iloc[i:i+30]
    correlation = fixed_window_ibm.corr(rolling_window_ge)
    rolling_correlations.append(correlation)

# Convert to DataFrame for easier plotting
rolling_cor_df = pd.DataFrame(rolling_correlations, index=GE.index[30 - 1:], columns=['Correlation'])

# Plot the rolling correlations
plt.plot(rolling_cor_df)
plt.title('Correlation of GE with IBM (Fixed Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
