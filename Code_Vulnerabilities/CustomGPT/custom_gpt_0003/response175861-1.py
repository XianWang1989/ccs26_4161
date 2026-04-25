
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM (e.g., days 1001-1030)
fixed_start = 1000  # Adjust index based on zero-indexing
fixed_window = IBM.iloc[fixed_start:fixed_start + 30]

# Initialize a list to store the correlations
correlations = []

# Calculate rolling correlations with the fixed window
for start in range(len(GE) - 30 + 1):
    rolling_window = GE.iloc[start:start + 30]  # Get the current 30-day window
    correlation = fixed_window.corr(rolling_window)
    correlations.append(correlation)

# Create a DataFrame for the correlations with corresponding dates
correlation_dates = GE.index[0:len(correlations)]  # Dates for each correlation
correlation_series = pd.Series(correlations, index=correlation_dates)

# Plot the rolling correlation
plt.figure(figsize=(10, 5))
plt.plot(correlation_series, label='Correlation between IBM (fixed window) and GE (rolling window)')
plt.title('Rolling Correlation between IBM and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axvline(x=GE.index[fixed_start], color='r', linestyle='--', label='Fixed Window Start')
plt.axvline(x=GE.index[fixed_start + 29], color='g', linestyle='--', label='Fixed Window End')
plt.legend()
plt.show()
