
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window from day 1001-1030 (adjust index as needed)
start_index = 1000  # Adjust this based on your DataFrame's index
end_index = 1030
fixed_window = IBM.iloc[start_index:end_index]

# Calculate rolling correlation
roll_cor = []
for i in range(len(GE) - len(fixed_window) + 1):
    rolling_segment = GE.iloc[i:i+len(fixed_window)]
    correlation = fixed_window.corr(rolling_segment)
    roll_cor.append(correlation.values[0])  # Assuming both series are 1D

# Create a new index for rolling correlation
correlation_index = GE.index[len(GE) - len(roll_cor):]

# Create a DataFrame for the results
roll_cor_df = pd.Series(roll_cor, index=correlation_index)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(roll_cor_df, label='Rolling Correlation (Fixed Window)', color='blue')
plt.title('Rolling Correlation of Fixed Window with Sliding Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
