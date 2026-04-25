
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the length of the rolling window
window_length = 30

# Create an empty list to store the correlations
correlation_results = []

# Calculate correlation for a fixed window of GE (days 1001-1030)
fixed_window_start = 1000
fixed_window_end = fixed_window_start + window_length

# Get the fixed window values for GE
fixed_ge_window = GE.iloc[fixed_window_start:fixed_window_end]

# Calculate correlation with rolling windows of IBM
for start in range(len(IBM) - window_length + 1):
    rolling_ibm_window = IBM.iloc[start:start + window_length]
    correlation = fixed_ge_window.corr(rolling_ibm_window)
    correlation_results.append(correlation)

# Convert the results to a DataFrame
correlation_df = pd.DataFrame(correlation_results, columns=['Correlation'], index=IBM.index[:len(correlation_results)])

# Plot the rolling correlations
plt.plot(correlation_df, label='Fixed GE Window Correlation')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.title('Correlation between Fixed GE Window and Rolling IBM Windows')
plt.legend()
plt.show()
