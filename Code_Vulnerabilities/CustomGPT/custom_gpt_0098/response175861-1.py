
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window
fixed_start = 1000  # Adjust this to your desired starting point
fixed_window = IBM[fixed_start:fixed_start + 30]

# Initialize a list to store correlations
correlations = []

# Loop through all possible 30-day windows in GE
for start in range(len(GE) - 29):  # Ensure we don't go out of bounds
    ge_window = GE[start:start + 30]
    correlation = fixed_window.corr(ge_window)
    correlations.append(correlation)

# Create a DataFrame for the correlations
correlation_index = GE.index[:len(correlations)]  # Align the index
correlation_series = pd.Series(correlations, index=correlation_index)

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation between Fixed IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
