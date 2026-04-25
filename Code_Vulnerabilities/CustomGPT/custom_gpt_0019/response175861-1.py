
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM (days 1001-1030)
start_index = 1000  # 0-based index for day 1001
fixed_window = IBM.iloc[start_index:start_index + 30]

# Prepare to store correlation results
correlations = []

# Iterate over possible 30-day windows in GE
for i in range(len(GE) - 30 + 1):
    rolling_window = GE.iloc[i:i + 30]
    corr = fixed_window.corr(rolling_window)
    correlations.append(corr)

# Convert correlations to a DataFrame for easier plotting
correlation_dates = GE.index[:len(correlations)]
correlation_results = pd.DataFrame(correlations, index=correlation_dates, columns=['Correlation'])

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(correlation_results, label='Correlation with IBM (fixed window)', color='blue')
plt.title('Rolling Correlation of GE with IBM (30-day fixed window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
