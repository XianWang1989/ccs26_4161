
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
start_fixed = 1000
end_fixed = 1030
GE_fixed = GE[start_fixed:end_fixed]

# Prepare a list to store correlations
correlations = []

# Loop through all possible 30-day windows in IBM
for start in range(len(IBM) - 29):  # Adjusting for 30-day window
    end = start + 30
    IBM_window = IBM[start:end]
    corr = GE_fixed.corr(IBM_window)
    correlations.append(corr)

# Convert correlations to a DataFrame for plotting
correlation_series = pd.Series(correlations, index=IBM.index[:len(correlations)])

# Plot the rolling correlations
plt.plot(correlation_series)
plt.title('Correlation Between GE (Days 1001-1030) and IBM 30-Day Windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
