
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for IBM
fixed_window_start = 1001  # specify your starting point
fixed_window_end = fixed_window_start + 30
IBM_fixed_window = IBM[fixed_window_start:fixed_window_end]

# Now we need to calculate rolling correlation for GE with this fixed window
correlation_results = []

# Iterate over the possible windows for GE
for start in range(len(GE) - 30 + 1):
    end = start + 30
    GE_window = GE[start:end]

    # Calculate the correlation for the fixed window of IBM and current GE window
    correlation = IBM_fixed_window.corr(GE_window)
    correlation_results.append(correlation)

# Convert the results into a DataFrame to visualize
correlation_df = pd.DataFrame(correlation_results, index=range(len(GE) - 30 + 1))

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(correlation_df)
plt.title("Rolling Correlation of Fixed IBM Window with Variable GE Windows")
plt.xlabel("GE Window Start Index")
plt.ylabel("Correlation")
plt.grid()
plt.show()
