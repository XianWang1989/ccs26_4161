
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window range for GE (e.g., days 1001-1030)
start_index = 1000  # Adjust as needed
constant_window = GE.iloc[start_index:start_index + 30]  # 30-day window

# Calculate rolling correlation
correlations = []
for end in range(30, len(IBM)):
    rolling_window = IBM.iloc[end - 30:end]  # 30-day window for IBM
    correlation = constant_window.corr(rolling_window)  # Calculate correlation
    correlations.append(correlation)

# Create a Series for plotting
correlation_series = pd.Series(correlations, index=IBM.index[30:len(IBM)])

# Plotting the rolling correlations
plt.figure(figsize=(10, 5))
plt.plot(correlation_series, label='Correlation with GE (Days 1001-1030)', color='blue')
plt.title('Rolling Correlation between IBM and GE (Fixed vs Varying Windows)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
