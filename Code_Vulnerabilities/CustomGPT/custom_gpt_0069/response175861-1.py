
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your stock data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window range
fixed_start = 1000  # Adjust based on your indexing
fixed_end = fixed_start + 30
fixed_window = IBM.iloc[fixed_start:fixed_end]

# Prepare to store correlations
correlations = []

# Loop through every possible 30-day window in GE
for i in range(len(GE) - 30 + 1):
    ge_window = GE.iloc[i:i + 30]
    correlation = fixed_window.corr(ge_window)
    correlations.append(correlation)

# Create a DataFrame for the correlations
correlation_series = pd.Series(correlations, index=GE.index[:len(correlations)])

# Plotting the correlations
plt.plot(correlation_series)
plt.title('Correlation between fixed IBM window and rolling GE window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
