
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Select a fixed window for IBM (days 1001-1030)
fixed_window_start = 1000  # This is the index for the start date, adjust as needed
fixed_window_end = fixed_window_start + 30
IBM_fixed = IBM.iloc[fixed_window_start:fixed_window_end]

# Initialize a list to store correlation results
correlations = []

# Loop through all possible 30-day windows in GE
for start in range(len(GE) - 30 + 1):
    GE_window = GE.iloc[start:start + 30]
    # Calculate correlation
    corr = IBM_fixed.corr(GE_window)
    correlations.append(corr)

# Create a DataFrame to store results with the rolling index based on GE
correlation_results = pd.Series(correlations, index=GE.index[:len(correlations)])

# Plot the correlations
plt.plot(correlation_results)
plt.title('Rolling Correlation of Fixed IBM Window with GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
