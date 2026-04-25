
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for GE, for example, days 1001-1030
fixed_window_start = 1000  # Change this based on your specific index
fixed_window_end = fixed_window_start + 30

# Get the fixed window prices for GE
fixed_window_GE = GE.iloc[fixed_window_start:fixed_window_end]

# Prepare a list to store the rolling correlations
rolling_correlations = []

# Loop over every possible 30-day window in IBM
for start in range(len(IBM) - 30 + 1):
    window_IBM = IBM.iloc[start:start + 30]
    correlation = fixed_window_GE.corr(window_IBM)
    rolling_correlations.append(correlation)

# Convert the results to a DataFrame
correlation_results = pd.DataFrame(rolling_correlations, index=range(len(IBM) - 30 + 1))

# Plot the results
plt.plot(correlation_results)
plt.title('Rolling Correlations between Fixed GE Window and IBM')
plt.xlabel('Days')
plt.ylabel('Correlation')
plt.show()
