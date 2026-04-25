
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the stock prices from a CSV file
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the window length for rolling correlation
window = 30
roll_cor = []

# Hold a constant 30-day window for GE and iterate through IBM
for start in range(len(IBM) - window + 1):
    # Extract the rolling window for IBM
    ibm_window = IBM.iloc[start:start + window]
    # Calculate the correlation with the fixed 30-day GE data
    correlation = ibm_window.corr(GE[start:start + window])
    roll_cor.append(correlation)

# Convert the results into a DataFrame
roll_cor_df = pd.DataFrame(roll_cor, index=IBM.index[:len(roll_cor)], columns=['Correlation'])

# Plot the rolling correlations
plt.plot(roll_cor_df, label='Rolling Correlation between GE and IBM')
plt.title('30-day Rolling Correlation of GE and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
