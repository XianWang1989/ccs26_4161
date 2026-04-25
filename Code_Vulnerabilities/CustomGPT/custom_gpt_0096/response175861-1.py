
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the start and end indices for the constant window
start_idx = 1000  # Replace with your actual start index
end_idx = start_idx + 30

# Extract the constant window for IBM
constant_window_ibm = IBM[start_idx:end_idx]

# Prepare a list to store correlations
correlations = []

# Loop through every possible 30-day window in GE
for i in range(len(GE) - 30 + 1):
    window_ge = GE[i:i + 30]
    corr = constant_window_ibm.corr(window_ge)  # Calculate correlation
    correlations.append(corr)

# Convert correlations to a DataFrame for further analysis
corr_df = pd.DataFrame(correlations, columns=['Correlation'], index=GE.index[:len(correlations)])

# Plot the correlations
plt.plot(corr_df.index, corr_df['Correlation'])
plt.title('Correlation of 30-day window of IBM with GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
