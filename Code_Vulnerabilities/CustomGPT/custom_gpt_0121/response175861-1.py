
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for IBM (example: days 1001-1030)
start_day = 1000  # Adjusted for zero-based indexing
end_day = start_day + 30

# Extract the constant window for IBM
IBM_window = IBM.iloc[start_day:end_day]

# Calculate the rolling correlations with GE
roll_cor = GE.rolling(window=30).corr(IBM_window)

# Plot the correlations
plt.figure(figsize=(12, 6))
plt.plot(roll_cor, label='Rolling Correlation of GE with IBM Window')
plt.title('Rolling Correlation of GE with Constant IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation Coefficient')
plt.legend()
plt.show()
