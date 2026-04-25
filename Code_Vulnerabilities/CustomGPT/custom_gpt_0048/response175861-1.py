
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window range
start = 1000  # Adjust based on your DataFrame index
end = start + 30

# Get the fixed window data for GE
fixed_window_GE = GE.iloc[start:end]

# Prepare an empty list to hold correlation values
correlations = []

# Loop through all possible 30-day windows in IBM
for i in range(len(IBM) - 30 + 1):
    rolling_window_IBM = IBM.iloc[i:i + 30]
    correlation = fixed_window_GE.corr(rolling_window_IBM)
    correlations.append(correlation)

# Convert correlations to a DataFrame for easier indexing
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the rolling correlation
plt.plot(correlation_series)
plt.title('Correlation between fixed GE window and rolling IBM windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
