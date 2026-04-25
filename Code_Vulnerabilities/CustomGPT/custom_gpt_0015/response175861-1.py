
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM
fixed_start = 1001
fixed_end = fixed_start + 30

# Get the fixed window for IBM
fixed_IBM = IBM.iloc[fixed_start:fixed_end]

# Prepare to store correlation results
correlations = []

# Calculate correlations for every possible 30-day window in GE
for start in range(len(GE) - 30 + 1):
    window_GE = GE.iloc[start:start + 30]
    correlation = fixed_IBM.corr(window_GE)
    correlations.append(correlation)

# Convert correlations to a DataFrame
correlation_df = pd.DataFrame(correlations, index=GE.index[:len(correlations)], columns=['Correlation'])

# Plot the rolling correlation results
plt.figure(figsize=(12, 6))
plt.plot(correlation_df.index, correlation_df['Correlation'], label='Correlation with IBM (Fixed Window)', color='b')
plt.title('Rolling Correlation between Fixed Window of IBM and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axhline(0, color='grey', linestyle='--')
plt.legend()
plt.show()
