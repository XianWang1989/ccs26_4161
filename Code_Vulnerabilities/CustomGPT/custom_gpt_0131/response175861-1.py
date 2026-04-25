
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Specify the fixed window for IBM (days 1001-1030)
fixed_window_start = 1000  # Index of day 1001
fixed_window_end = 1030     # Index of day 1030

# Extract the fixed window of IBM prices
fixed_window_ibm = IBM.iloc[fixed_window_start:fixed_window_end]

# Initialize an empty list to hold the correlation values
correlation_values = []

# Calculate the rolling correlation
for i in range(len(GE) - 30 + 1):
    window_ge = GE.iloc[i:i + 30]
    correlation = fixed_window_ibm.corr(window_ge)
    correlation_values.append(correlation)

# Convert correlation values into a Series
correlation_series = pd.Series(correlation_values, index=GE.index[30-1:])

# Plot the correlation results
plt.plot(correlation_series)
plt.title('Rolling Correlation between Fixed IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
