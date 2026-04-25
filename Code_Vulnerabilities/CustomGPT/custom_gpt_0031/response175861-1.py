
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE (e.g., days 1001-1030)
start = 1000  # Starting index for GE
end = 1030    # Ending index for GE
constant_GE = GE[start:end]

# Create a list to hold the correlation results
correlations = []

# Calculate the correlation for every possible 30-day window in IBM
for i in range(len(IBM) - 30 + 1):
    windowed_IBM = IBM[i:i + 30]
    correlation = constant_GE.corr(windowed_IBM)
    correlations.append(correlation)

# Convert results to a DataFrame for easy handling
correlation_df = pd.DataFrame(correlations, index=IBM.index[:len(correlations)], columns=['Correlation'])

# Plot the results
plt.plot(correlation_df)
plt.title('Rolling Correlation between IBM and Constant GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
