
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for GE
fixed_window_start = 1000  # Adjust this according to your DataFrame index
fixed_window_end = fixed_window_start + 30

# Extract the fixed window for GE
fixed_GE = GE.iloc[fixed_window_start:fixed_window_end]

# Prepare a list to store rolling correlations
rolling_correlations = []

# Compute rolling correlation
for start in range(len(IBM) - 30 + 1):  # Adjust range to prevent out-of-bounds
    current_window_IBM = IBM.iloc[start:start + 30]
    corr = current_window_IBM.corr(fixed_GE)
    rolling_correlations.append(corr)

# Create a DataFrame to hold rolling correlations with corresponding dates
dates = IBM.index[0:len(rolling_correlations)]  # Create dates based on the length of rolling correlations
rolling_cor_df = pd.DataFrame(rolling_correlations, index=dates, columns=['Correlation'])

# Plot the rolling correlation
plt.plot(rolling_cor_df, label='Correlation with GE (fixed window)')
plt.title('Rolling Correlation of IBM with Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
