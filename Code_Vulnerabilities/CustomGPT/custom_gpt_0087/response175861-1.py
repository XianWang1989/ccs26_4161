
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window start and end dates
fixed_start = '2019-01-01'  # Change this to your required start date
fixed_end = '2019-01-30'    # Change this to your required end date

# Slice the fixed window for GE
ge_fixed = GE[fixed_start:fixed_end]

# Calculate rolling correlation
rolling_corrs = []
for i in range(len(IBM) - 30 + 1):
    ibm_window = IBM[i:i+30]
    corr = ibm_window.corr(ge_fixed)
    rolling_corrs.append(corr)

# Create a Series for plotting
rolling_corr_series = pd.Series(rolling_corrs, index=IBM.index[0:len(rolling_corrs)])

# Plot the rolling correlation
plt.plot(rolling_corr_series)
plt.title('Rolling Correlation of GE Fixed Window with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
