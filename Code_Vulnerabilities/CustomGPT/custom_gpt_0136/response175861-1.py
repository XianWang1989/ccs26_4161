
import pandas as pd
import matplotlib.pyplot as plt

# Read the stock prices from CSV
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE (e.g., days 1001-1030)
start_date = 'YYYY-MM-DD'  # Replace with the start date of your window
end_date = 'YYYY-MM-DD'    # Replace with the end date

# Slicing the GE data for the constant window
GE_window = GE[start_date:end_date]

# Initialize a list to store the correlations
correlations = []

for i in range(len(IBM) - 30 + 1):
    IBM_window = IBM[i:i + 30]
    correlation = GE_window.corr(IBM_window)
    correlations.append(correlation)

# Create a date index for the results
dates = IBM.index[:len(correlations)]

# Convert to DataFrame for easy plotting
correlation_series = pd.Series(correlations, index=dates)

# Plot the rolling correlation
plt.plot(correlation_series)
plt.title('Correlation of GE (Constant Window) with IBM (Rolling Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
