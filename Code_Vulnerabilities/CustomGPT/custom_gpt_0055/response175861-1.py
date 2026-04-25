
import pandas as pd
import matplotlib.pyplot as plt

# Read the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Specify the constant window for GE (for example, days 1001-1030)
constant_start = 1000  # index starts at 0
constant_end = constant_start + 30

# Extract the constant window of GE
ge_window = GE[constant_start:constant_end]

# Prepare to store rolling correlations
rolling_correlations = []

# Iterate over each possible 30-day window in IBM
for start in range(len(IBM) - 29):
    ibm_window = IBM[start:start + 30]
    correlation = ge_window.corr(ibm_window)
    rolling_correlations.append(correlation)

# Convert the rolling correlations to a DataFrame for better visualization
rolling_cor_df = pd.DataFrame(rolling_correlations, index=IBM.index[:len(rolling_correlations)])

# Plot the results
plt.plot(rolling_cor_df)
plt.title('Rolling Correlation between GE (fixed window) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
