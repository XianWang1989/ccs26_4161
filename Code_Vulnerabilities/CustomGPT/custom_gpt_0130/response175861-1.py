
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (e.g., days 1001-1030)
fixed_start = 1000  # Adjust based on your index
fixed_end = fixed_start + 30

# Extract the fixed window for GE
ge_fixed_window = GE.iloc[fixed_start:fixed_end]

# Calculate rolling correlation
corr_results = []
for start in range(len(IBM) - 30 + 1):
    ibm_window = IBM.iloc[start:start + 30]
    corr = ge_fixed_window.corr(ibm_window)
    corr_results.append(corr)

# Convert results to a DataFrame
corr_df = pd.DataFrame(corr_results, columns=['Correlation'], index=IBM.index[:len(corr_results)])

# Plot results
plt.plot(corr_df.index, corr_df['Correlation'])
plt.title('Rolling Correlation of GE (Fixed Window) with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
