
import pandas as pd
import matplotlib.pyplot as plt

# Load your stock price data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE (for example, days 1001-1030)
start_index = 1000  # Adjust based on your data's index (0-based)
constant_window_GE = GE.iloc[start_index:start_index + 30]

# Initialize a list to store correlations
correlations = []

# Calculate correlations with sliding windows of IBM
for i in range(len(IBM) - 30):
    window_IBM = IBM.iloc[i:i + 30]
    correlation = constant_window_GE.corr(window_IBM)
    correlations.append(correlation)

# Create a DataFrame for better visualization
correlation_series = pd.Series(correlations, index=IBM.index[0:len(correlations)])  # Aligning index

# Plotting the rolling correlations
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE (Constant Window) with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
