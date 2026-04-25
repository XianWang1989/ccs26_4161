
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for GE (e.g., days 1001-1030)
start_date = '1001-01-01'  # Adjust according to your actual date format
end_date = '1001-01-30'
fixed_window = GE[start_date:end_date]

# Initialize a list to hold the rolling correlations
rolling_correlations = []

# Calculate the rolling correlation
for i in range(len(IBM) - 30 + 1):
    current_window = IBM[i:i + 30]
    correlation = fixed_window.corr(current_window)
    rolling_correlations.append(correlation)

# Create a DataFrame for rolling correlations
correlation_series = pd.Series(rolling_correlations, index=IBM.index[0:len(rolling_correlations)])

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation between Fixed GE Window and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
