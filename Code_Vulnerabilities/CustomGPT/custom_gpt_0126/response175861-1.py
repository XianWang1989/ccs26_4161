
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
fixed_start = 1000  # Starting index for GE (adjust based on your data)
fixed_end = fixed_start + 30

# Extract the fixed 30-day window for GE
fixed_GE_window = GE.iloc[fixed_start:fixed_end]

# Prepare to store correlations
correlations = []

# Iterate over all possible 30-day windows for IBM
for start in range(len(IBM) - 30):
    end = start + 30
    rolling_IBM_window = IBM.iloc[start:end]

    # Calculate correlation
    corr = fixed_GE_window.corr(rolling_IBM_window)
    correlations.append(corr)

# Create a DataFrame of correlations
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(correlation_series)
plt.title('Correlation between Fixed GE Window and IBM Rolling Windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
