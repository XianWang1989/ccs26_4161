
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select the stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the range for the fixed window in GE
start_day = 1000  # Index for the start of the GE window (assuming 0-based index)
end_day = start_day + 30

# Create the fixed window series for GE
ge_window = GE.iloc[start_day:end_day]

# List to store rolling correlations
rolling_correlations = []

# Calculate the correlation with each possible 30-day window in IBM
for i in range(len(IBM) - 29):  # Ensure we stay within bounds
    ibm_window = IBM.iloc[i:i + 30]
    correlation = ge_window.corr(ibm_window)
    rolling_correlations.append(correlation)

# Convert list to a DataFrame for easier plotting and analysis
correlation_index = pd.date_range(start=IBM.index[0], periods=len(rolling_correlations), freq='D')[:len(rolling_correlations)]
rolling_corr_df = pd.DataFrame(rolling_correlations, index=correlation_index, columns=['Correlation'])

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(rolling_corr_df.index, rolling_corr_df['Correlation'], label='Correlation with GE (Days 1001-1030)', color='blue')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.title('Rolling Correlation of IBM with GE Fixed Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.grid()
plt.show()
