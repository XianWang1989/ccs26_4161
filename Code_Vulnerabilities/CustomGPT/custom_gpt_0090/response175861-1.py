
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (e.g., days 1001-1030)
fixed_start = 1000  # Adjust based on your index
fixed_end = fixed_start + 30
ge_fixed_window = GE.iloc[fixed_start:fixed_end]

# Calculate rolling correlations with GE's fixed window against IBM
roll_cor = []
for i in range(len(IBM) - 30 + 1):
    ibm_window = IBM.iloc[i:i + 30]
    correlation = ge_fixed_window.corr(ibm_window)
    roll_cor.append(correlation)

# Create a DataFrame for results
results = pd.DataFrame(roll_cor, index=IBM.index[:len(roll_cor)], columns=['Correlation'])

# Plot the rolling correlation
plt.plot(results)
plt.title('Rolling Correlation of IBM with Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
