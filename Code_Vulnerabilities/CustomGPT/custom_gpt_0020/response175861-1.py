
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the stock prices CSV and set the date as index
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Extract the stock prices for IBM and GE
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define your constant window
constant_window_start = 1000  # for example, starting at index 1000
constant_window_end = 1030     # ending at index 1030 (30 days later)

# Slice the constant window for GE
ge_constant_window = GE.iloc[constant_window_start:constant_window_end]

# Prepare an empty list to store the correlation results
correlation_results = []

# Loop through possible windows in IBM
for i in range(len(IBM) - 30):
    ibm_window = IBM.iloc[i:i + 30]  # Get a rolling window of 30 days for IBM
    corr = ge_constant_window.corr(ibm_window)  # Calculate correlation
    correlation_results.append(corr)

# Create a DataFrame for the correlations with appropriate index
correlation_df = pd.DataFrame(correlation_results, index=IBM.index[:len(correlation_results)], columns=['Correlation'])

# Plot the correlation results
plt.plot(correlation_df.index, correlation_df['Correlation'])
plt.title('Rolling Correlation between GE (Fixed) and IBM (Rolling)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
