
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window and correlation list
fixed_window = GE[1000:1030]  # Adjust the index as needed
roll_cor = []

# Loop through all possible windows in IBM
for i in range(len(IBM) - 30 + 1):  # Ensure we have enough data for a window
    rolling_window = IBM[i:i+30]
    corr = rolling_window.corr(fixed_window)
    roll_cor.append(corr)

# Create a new DataFrame for correlation results
correlation_df = pd.DataFrame(roll_cor, index=IBM.index[:len(roll_cor)], columns=['Correlation'])

# Plot the results
plt.plot(correlation_df)
plt.title('Rolling Correlation between GE (fixed window) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
