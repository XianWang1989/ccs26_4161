
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the start and end of the constant window
start_day = 1000  # Adjust for zero-based index
end_day = start_day + 30

# Extract the constant 30-day window for IBM
constant_window_IBM = IBM[start_day:end_day]

# Prepare to store correlations
correlations = []

# Loop through all possible 30-day windows in GE
for start in range(len(GE) - 30 + 1):
    end = start + 30
    window_GE = GE[start:end]
    correlation = constant_window_IBM.corr(window_GE)  # Calculate the correlation
    correlations.append(correlation)

# Convert correlations to a DataFrame for plotting
correlation_series = pd.Series(correlations, index=GE.index[:len(correlations)])

# Plot the rolling correlations
plt.figure(figsize=(10, 5))
plt.plot(correlation_series)
plt.title('Correlation between 30-day window of IBM and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axvline(x=IBM.index[start_day], color='r', linestyle='--', label='Start of Constant Window')
plt.legend()
plt.show()
