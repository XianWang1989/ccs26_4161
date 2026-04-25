
import pandas as pd
import matplotlib.pyplot as plt

# Load your stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE
const_start = 1000  # Starting index for constant window
const_end = const_start + 30  # End index for the constant window

# Extract the constant window for GE
GE_const_window = GE[const_start:const_end]

# Initialize an empty list to hold correlations
correlations = []

# Iterate through the range of possible windows for IBM
for start in range(len(IBM) - 30):
    IBM_window = IBM[start:start + 30]
    correlation = GE_const_window.corr(IBM_window)  # Calculate correlation
    correlations.append(correlation)

# Convert to a DataFrame for easier plotting
correlation_series = pd.Series(correlations, index=range(len(correlations)))

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(correlation_series)
plt.title('Rolling Correlation between Constant 30-Day GE and IBM')
plt.xlabel('Start Index for IBM (variable window)')
plt.ylabel('Correlation')
plt.axvline(x=1000, color='r', linestyle='--', label='GE Fixed Window Start')
plt.legend()
plt.show()
