
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Define the stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for IBM (days 1001-1030)
fixed_start = IBM.index[1000]  # Start at index 1000 (1001 day)
fixed_end = IBM.index[1029]    # End at index 1029 (1030 day)
fixed_window_ibm = IBM[fixed_start:fixed_end]

# Prepare to store the correlation values
correlations = []

# Iterate through each possible 30-day window of GE
for start in range(len(GE) - 30 + 1):
    end = start + 30
    rolling_window_ge = GE[start:end]

    # Calculate the correlation with the fixed IBM window
    correlation = fixed_window_ibm.corr(rolling_window_ge)
    correlations.append(correlation)

# Create a new index for the correlations (aligned with GE windows)
correlation_index = GE.index[:len(correlations)]

# Create a DataFrame for better visualization
correlation_df = pd.DataFrame(correlations, index=correlation_index)

# Plot the correlations
plt.plot(correlation_df)
plt.title("Correlation of Fixed IBM Window with Rolling GE Windows")
plt.xlabel("Date")
plt.ylabel("Correlation")
plt.show()
