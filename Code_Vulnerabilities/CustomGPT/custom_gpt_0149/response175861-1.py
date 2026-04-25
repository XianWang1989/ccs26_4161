
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (e.g., days 1001-1030)
fixed_window_start = 1000  # Adjust as necessary based on your index
fixed_window_end = fixed_window_start + 30

# Slice the fixed window of GE
fixed_GE = GE.iloc[fixed_window_start:fixed_window_end]

# Initialize a list to store correlations
correlations = []

# Calculate rolling correlation with the fixed window
for start in range(len(IBM) - 29):  # 29 to ensure a 30-day window
    windowed_IBM = IBM[start:start + 30]
    corr = fixed_GE.corr(windowed_IBM)
    correlations.append(corr)

# Create a DataFrame for the rolling correlations
rolling_corr_df = pd.DataFrame(correlations, index=IBM.index[:len(correlations)], columns=['Correlation'])

# Plot the rolling correlations
plt.plot(rolling_corr_df)
plt.title('Rolling Correlation of Fixed GE Window with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
