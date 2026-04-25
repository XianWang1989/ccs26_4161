
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Specify the constant window for GE
start = 1000  # Adjust according to your index
window = 30

# Extract the fixed window for GE
fixed_window_GE = GE[start:start + window]

# Initialize a list to store correlations
correlations = []

# Iterate through all possible 30-day windows in IBM
for i in range(len(IBM) - window + 1):
    current_window_IBM = IBM[i:i + window]
    corr = np.corrcoef(fixed_window_GE, current_window_IBM)[0, 1]
    correlations.append(corr)

# Create a DataFrame for the correlations
correlation_df = pd.DataFrame(correlations, index=IBM.index[:len(correlations)])

# Plot the rolling correlations
plt.plot(correlation_df)
plt.title('Rolling Correlation between GE (Days 1001-1030) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
