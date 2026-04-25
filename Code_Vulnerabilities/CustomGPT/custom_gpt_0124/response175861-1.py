
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window
fixed_start = 1000  # Starting index for IBM
fixed_window = IBM.iloc[fixed_start:fixed_start + 30]

# Calculate rolling correlation with every possible 30-day window in GE
rolling_correlations = []

for start in range(len(GE) - 30 + 1):
    ge_window = GE.iloc[start:start + 30]
    correlation = fixed_window.corr(ge_window)
    rolling_correlations.append(correlation)

# Convert results to a DataFrame for easier plotting
rolling_correlations_df = pd.DataFrame(rolling_correlations, index=GE.index[0:len(rolling_correlations)], columns=['Correlation'])

# Plot the rolling correlations
plt.plot(rolling_correlations_df)
plt.title('Rolling Correlation between Fixed IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
