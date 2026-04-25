
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window
start_date = '2001-01-01'  # Example start date for the fixed window
end_date = '2001-01-30'    # Example end date for the fixed window
fixed_window = GE[start_date:end_date]

# Calculate rolling correlation with fixed window
correlations = []
for i in range(len(IBM) - len(fixed_window) + 1):
    rolling_window = IBM[i:i + len(fixed_window)]
    correlation = rolling_window.corr(fixed_window)
    correlations.append(correlation)

# Create a Series to align with the IBM index for plotting
correlation_series = pd.Series(correlations, index=IBM.index[len(fixed_window)-1:])

# Plot the correlation
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE (fixed window) with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
