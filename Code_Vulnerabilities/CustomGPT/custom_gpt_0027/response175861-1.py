
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM (for example, days 1001-1030)
fixed_start = 1000  # Adjust based on your index
fixed_end = 1030

# Extract the fixed window for IBM
fixed_IBM_window = IBM.iloc[fixed_start:fixed_end]

# Prepare a list to store correlation results
correlation_results = []

# Loop over all possible 30-day windows in GE
for start in range(len(GE) - 30 + 1):
    rolling_GE_window = GE.iloc[start:start + 30]
    correlation = fixed_IBM_window.corr(rolling_GE_window)
    correlation_results.append(correlation)

# Convert results into a DataFrame for better visualization
correlation_df = pd.DataFrame(correlation_results, columns=['Correlation'])
correlation_df.index = range(len(GE) - 30 + 1)

# Plot the correlation results
plt.plot(correlation_df)
plt.title('Correlation between Fixed IBM Window and Rolling GE Windows')
plt.xlabel('Rolling GE Window Start Index')
plt.ylabel('Correlation')
plt.show()
