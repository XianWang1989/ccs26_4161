
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select the two stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window start and end dates for IBM (example: days 1001-1030)
start_date = IBM.index[1000]  # Assuming 0-based indexing
end_date = IBM.index[1030 - 1]  # Adjust for inclusive end
IBM_window = IBM.loc[start_date:end_date]

# Prepare to store correlations
correlations = []

# Loop through every possible 30-day window in the GE stock prices
for i in range(len(GE) - 30 + 1):
    GE_window = GE[i:i + 30]
    corr = IBM_window.corr(GE_window)
    correlations.append(corr)

# Create a DataFrame to hold the results
correlation_results = pd.DataFrame(correlations, index=GE.index[:len(correlations)])

# Plot the correlations
plt.plot(correlation_results, label='Correlation with IBM (fixed window)', color='blue')
plt.title('Rolling Correlation of GE with IBM 30-day Window')
plt.xlabel('Date')
plt.ylabel('Correlation Coefficient')
plt.legend()
plt.show()
