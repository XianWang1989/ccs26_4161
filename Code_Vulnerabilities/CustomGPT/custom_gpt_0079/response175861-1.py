
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window
start_index = 1000  # Adjust this to your desired start
end_index = start_index + 30

# Slice the constant window for GE
constant_window_GE = GE[start_index:end_index]

# Prepare to store rolling correlations
rolling_correlations = []

# Loop through every possible 30-day window of IBM
for i in range(len(IBM) - 30 + 1):
    window_IBM = IBM[i:i + 30]
    # Calculate the correlation
    corr = constant_window_GE.corr(window_IBM)
    rolling_correlations.append(corr)

# Create a Series for the correlations with proper indexing
rolling_cor_series = pd.Series(rolling_correlations, index=IBM.index[:len(rolling_correlations)])

# Plot the results
plt.plot(rolling_cor_series)
plt.title('Rolling Correlation between IBM and constant GE window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
