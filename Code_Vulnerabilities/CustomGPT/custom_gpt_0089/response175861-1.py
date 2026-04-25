
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices from CSV
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
fixed_window_start = 1000
fixed_window_end = fixed_window_start + 30

# Extract the constant window for GE
ge_fixed_window = GE.iloc[fixed_window_start:fixed_window_end]

# Initialize a list to hold correlations
correlations = []

# Loop through all possible 30-day windows in IBM
for start in range(len(IBM) - 30 + 1):
    ibm_window = IBM.iloc[start:start + 30]

    # Calculate correlation with the fixed GE window
    correlation = np.corrcoef(ibm_window, ge_fixed_window)[0, 1]
    correlations.append(correlation)

# Create a DataFrame for easier plotting
correlation_series = pd.Series(correlations, index=range(len(correlations)))

# Plot the correlations
plt.plot(correlation_series)
plt.title('Rolling Correlation of IBM with a Fixed 30-day Window of GE')
plt.xlabel('Starting Day of IBM Window')
plt.ylabel('Correlation')
plt.show()
