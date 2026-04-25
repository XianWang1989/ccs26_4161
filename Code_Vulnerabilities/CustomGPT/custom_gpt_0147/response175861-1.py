
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices DataFrame.
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM.
start_ibm = 1000  # Start of the fixed window for IBM (index-based)
end_ibm = 1030    # End of the fixed window for IBM (index-based)

# Get the fixed 30-day data for IBM.
ibm_fixed_window = IBM.iloc[start_ibm:end_ibm]

# Prepare a list to hold correlation values.
correlations = []

# Iterate through the GE stock data with a rolling window.
for i in range(len(GE) - 29):  # Make sure the window fits within GE's length
    ge_window = GE.iloc[i:i+30]  # Get a 30-day window for GE
    correlation = ibm_fixed_window.corr(ge_window).iloc[0, 0]  # Compute correlation
    correlations.append(correlation)

# Plotting the correlations over time.
plt.figure(figsize=(12, 6))
plt.plot(range(len(correlations)), correlations, label='Rolling Correlation (GE vs Fixed IBM Window)')
plt.xlabel('Start Index (of GE 30-day window)')
plt.ylabel('Correlation')
plt.title('Rolling Correlation between fixed IBM window and GE')
plt.legend()
plt.grid()
plt.show()
