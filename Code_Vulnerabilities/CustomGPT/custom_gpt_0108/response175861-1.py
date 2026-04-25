
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window range for IBM (e.g., days 1001-1030)
fixed_start = 1000  # 1001 in 0-based index
fixed_end = 1030    # 1030 in 0-based index

# Slice the fixed window for IBM
fixed_window_IBM = IBM.iloc[fixed_start:fixed_end]

# Prepare a list to store correlation results
correlations = []

# Calculate rolling correlation for GE with the fixed IBM window
for i in range(len(GE) - 29):  # Ensuring a full 30-day window
    rolling_window_GE = GE.iloc[i:i + 30]
    correlation = fixed_window_IBM.corr(rolling_window_GE)
    correlations.append(correlation)

# Create a Series for plotting with the proper index
roll_cor_series = pd.Series(correlations, index=GE.index[0:len(correlations)])

# Plot the rolling correlations
plt.plot(roll_cor_series)
plt.title('Rolling Correlation between Fixed IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
