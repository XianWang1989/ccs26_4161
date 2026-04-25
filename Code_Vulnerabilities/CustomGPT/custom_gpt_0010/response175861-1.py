
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the range for the constant window
constant_start = 1000  # Change this to your desired start index
constant_end = constant_start + 30

# Extract the constant window for IBM
constant_window_IBM = IBM.iloc[constant_start:constant_end]

# Calculate rolling correlations with the constant window against GE
rolling_correlations = []
for start in range(len(GE) - 30 + 1):
    current_window_GE = GE.iloc[start:start + 30]
    correlation = constant_window_IBM.corr(current_window_GE)
    rolling_correlations.append(correlation)

# Convert to a DataFrame for easier plotting
rolling_cor_df = pd.DataFrame(rolling_correlations, index=GE.index[:len(rolling_correlations)])

# Plot the rolling correlations
plt.plot(rolling_cor_df)
plt.title('Rolling Correlation of GE with Fixed IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
