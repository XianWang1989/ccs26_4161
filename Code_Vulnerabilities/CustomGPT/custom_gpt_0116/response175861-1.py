
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Fixed window (example: days 1001-1030)
fixed_start = 1000  # Zero-based index (e.g., row 1001 in CSV)
fixed_end = fixed_start + 30
fixed_window = IBM.iloc[fixed_start:fixed_end]

# List to hold correlation values
correlations = []

# Iterate over possible start points for GE
for start in range(len(GE) - 30 + 1):
    rolling_window = GE.iloc[start:start + 30]
    correlation = fixed_window.corr(rolling_window).iloc[0, 0]  # Get the correlation value
    correlations.append(correlation)

# Create a DataFrame for visualization
correlation_df = pd.DataFrame(correlations, index=range(len(GE) - 30 + 1), columns=['Correlation'])

# Plot the results
plt.plot(correlation_df)
plt.title('Correlation between Fixed Window of IBM and Rolling Window of GE')
plt.xlabel('GE Rolling Start Index')
plt.ylabel('Correlation')
plt.show()
