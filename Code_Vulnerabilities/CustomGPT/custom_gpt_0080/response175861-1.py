
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window range for GE
start_date = 1000  # Adjust as needed
end_date = start_date + 30
fixed_GE_window = GE[start_date:end_date]

# Calculate rolling correlation
rolling_correlations = []

for i in range(len(IBM) - 30):
    IBM_window = IBM[i:i + 30]
    corr = fixed_GE_window.corr(IBM_window)
    rolling_correlations.append(corr)

# Create a Series for the correlation results
roll_cor_series = pd.Series(rolling_correlations, index=IBM.index[:len(rolling_correlations)])

# Plot the rolling correlations
plt.plot(roll_cor_series)
plt.title('Rolling Correlation with Constant GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
