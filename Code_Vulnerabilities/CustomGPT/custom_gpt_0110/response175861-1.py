
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window (e.g., days 1001-1030)
start_index = 1000  # Adjust based on your data
end_index = start_index + 30

# Slicing the constant window for IBM
constant_window_IBM = IBM.iloc[start_index:end_index]

# Initialize a list to store correlations
correlations = []

# Loop through all possible 30-day windows in GE
for start in range(len(GE) - 30 + 1):
    window_GE = GE.iloc[start:start + 30]
    correlation = constant_window_IBM.corr(window_GE)
    correlations.append(correlation)

# Convert correlations to a DataFrame for easier plotting
correlation_series = pd.Series(correlations, index=GE.index[:len(correlations)]) 

# Plot the correlations
plt.plot(correlation_series)
plt.title('Correlation of GE with a Fixed Window of IBM Prices')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
