
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window range for GE (e.g., days 1001-1030)
start_day = 1000  # Adjust index based on your DataFrame starting index
end_day = 1030

# Extract the fixed window for GE
fixed_GE_window = GE.iloc[start_day:end_day]

# Initialize an array to store correlations
correlations = []

# Loop through all possible 30-day windows in IBM
for i in range(len(IBM) - 29):  # Subtract 29 to avoid index overflow
    rolling_IBM_window = IBM.iloc[i:i + 30]
    correlation = fixed_GE_window.corr(rolling_IBM_window)
    correlations.append(correlation)

# Convert correlations to a Pandas Series for easier plotting
correlation_series = pd.Series(correlations, index=IBM.index[0:len(correlations)])

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(correlation_series)
plt.title('Rolling Correlation of Fixed GE Window with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid()
plt.show()
