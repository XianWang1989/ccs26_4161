
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
fixed_start = 1000  # Adjust based on 0-indexing
fixed_end = fixed_start + 30  # 30-day window

# Extract the constant window for GE
fixed_GE = GE.iloc[fixed_start:fixed_end]

# Prepare a list to hold correlation values
correlations = []

# Iterate over every possible rolling window in IBM
for i in range(len(IBM) - 30):
    # Get the current rolling window
    rolling_IBM = IBM.iloc[i:i + 30]
    # Calculate the correlation
    corr = fixed_GE.corr(rolling_IBM)
    correlations.append(corr)

# Create a DataFrame for correlations with dates
correlation_dates = IBM.index[30:len(IBM)]
correlation_df = pd.DataFrame(correlations, index=correlation_dates, columns=['Correlation'])

# Plot the results
plt.plot(correlation_df)
plt.title('Correlation between Fixed GE Window and Rolling IBM Windows')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
