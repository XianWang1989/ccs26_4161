
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Fixed window for IBM
start_index = 1000  # Adjusted for zero-based index
end_index = start_index + 30
fixed_ibm_window = IBM.iloc[start_index:end_index]

# Prepare to store correlation results
correlations = []
dates = []

# Calculate correlation for every possible 30-day window of GE
for i in range(len(GE) - 29):  # Ensures we don't go out of bounds
    current_ge_window = GE.iloc[i:i + 30]
    corr = fixed_ibm_window.corr(current_ge_window)
    correlations.append(corr)
    dates.append(current_ge_window.index[-1])  # Use the end date of the current window

# Create a DataFrame for the results
result_df = pd.DataFrame({'Date': dates, 'Correlation': correlations})
result_df.set_index('Date', inplace=True)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(result_df.index, result_df['Correlation'])
plt.title('Rolling Correlation between Fixed IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid()
plt.show()
