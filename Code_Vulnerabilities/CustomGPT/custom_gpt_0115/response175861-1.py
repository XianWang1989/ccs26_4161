
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM
start_index = 1000  # Adjust as needed (Python indexing starts at 0)
fixed_window = IBM[start_index:start_index + 30]

# Prepare a list to store correlations
correlations = []

# Loop through GE to calculate correlations with the fixed IBM window
for i in range(len(GE) - 30 + 1):
    current_window = GE[i:i + 30]
    corr = fixed_window.corr(current_window)
    correlations.append(corr)

# Convert the correlations list to a Series for easier plotting
correlation_series = pd.Series(correlations, index=GE.index[0:len(correlations)])

# Plot the results
plt.plot(correlation_series)
plt.title('Rolling Correlation of GE with Fixed IBM 30-Day Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
