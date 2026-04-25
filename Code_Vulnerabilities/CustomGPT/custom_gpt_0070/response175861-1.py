
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for one stock
fixed_window = IBM[1000:1030]  # Days 1001-1030, adjust if you need 0-indexing

# Prepare a DataFrame to store the rolling correlations
rolling_correlations = []

# Calculate the rolling correlation for the fixed window with each possible 30-day window of GE
for start in range(len(GE) - 29):
    rolling_window = GE[start:start + 30]
    correlation = fixed_window.corr(rolling_window)
    rolling_correlations.append(correlation)

# Create a DataFrame for the results
results = pd.DataFrame(rolling_correlations, index=GE.index[0:len(rolling_correlations)], columns=['Correlation'])

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(results.index, results['Correlation'], label='Rolling Correlation with IBM (Days 1001-1030)', color='blue')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.title('Rolling Correlation between IBM and GE Fixed Window')
plt.legend()
plt.show()
