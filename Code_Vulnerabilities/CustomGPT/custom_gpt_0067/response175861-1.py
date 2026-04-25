
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define fixed window for GE
start_date = '2001-01-01'  # adjust based on your data
end_date = '2001-01-30'     # adjust based on your data
fixed_ge_window = GE[start_date:end_date]

# Prepare to store correlations
correlations = []

# Loop through the IBM rolling windows
for i in range(len(IBM) - 30 + 1):
    ibm_window = IBM[i:i+30]  # Get the rolling 30-day window
    correlation = fixed_ge_window.corr(ibm_window)  # Calculate correlation
    correlations.append(correlation)

# Create a DataFrame for correlation results
correlation_index = IBM.index[29:]  # Adjust index to align with results
correlation_series = pd.Series(correlations, index=correlation_index)

# Plot the results
plt.plot(correlation_series)
plt.title('Correlation between fixed GE window and rolling IBM windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
