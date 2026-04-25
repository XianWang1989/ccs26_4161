
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (days 1001-1030)
fixed_window_start = 1000  # Adjusted for zero-based index
fixed_window_end = fixed_window_start + 30

# Extract the fixed window for GE
fixed_ge_window = GE.iloc[fixed_window_start:fixed_window_end]

# Initialize a list to store correlations
correlations = []

# Loop through every possible 30-day window in IBM
for start in range(len(IBM) - 29):  # Ensure there's enough data for a 30-day window
    ibm_window = IBM[start:start + 30]
    correlation = fixed_ge_window.corr(ibm_window)
    correlations.append(correlation)

# Convert to a DataFrame for easier plotting
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the correlations
plt.plot(correlation_series)
plt.title('Correlation between GE (Days 1001-1030) and Rolling Windows of IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
