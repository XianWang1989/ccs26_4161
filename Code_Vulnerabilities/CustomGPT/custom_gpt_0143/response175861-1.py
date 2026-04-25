
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window
fixed_start = 1000  # Adjust to your specific needs (0-indexed)
fixed_end = fixed_start + 30

# Select the fixed window for IBM
fixed_window_IBM = IBM.iloc[fixed_start:fixed_end]

# Prepare a list to store correlations
correlations = []

# Slide over the GE stock data for rolling windows
for i in range(len(GE) - 30 + 1):
    window_GE = GE.iloc[i:i + 30]
    correlation = fixed_window_IBM.corr(window_GE)
    correlations.append(correlation)

# Create a DataFrame to hold the results
results = pd.DataFrame(correlations, index=GE.index[0:len(correlations)], columns=['Correlation'])

# Plot the results
plt.plot(results.index, results['Correlation'])
plt.title('Rolling Correlation between Fixed IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axhline(0, color='red', linestyle='--')
plt.show()
