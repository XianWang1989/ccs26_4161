
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window
fixed_window_start = 1001
fixed_window_end = fixed_window_start + 30

# Extract the fixed window data for IBM
fixed_window_IBM = IBM[fixed_window_start:fixed_window_end]

# Prepare a list to store the correlation results
correlations = []

# Loop through all possible 30-day windows in GE
for start in range(len(GE) - 30 + 1):
    end = start + 30
    rolling_window_GE = GE[start:end]

    # Calculate the correlation and append it to the list
    correlation = fixed_window_IBM.corr(rolling_window_GE)
    correlations.append(correlation)

# Create a DataFrame for correlations
correlation_results = pd.DataFrame(correlations, index=GE.index[30-1:], columns=['Correlation'])

# Plot the correlation results
plt.plot(correlation_results)
plt.title('Correlation between Fixed 30-Day IBM Window and Rolling GE Windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid()
plt.show()
