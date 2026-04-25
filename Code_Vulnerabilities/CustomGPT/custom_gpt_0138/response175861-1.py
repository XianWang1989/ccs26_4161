
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for IBM (e.g., days 1001-1030)
start_index = 1000  # Adjust according to your DataFrame's time index
end_index = start_index + 30
ibm_window = IBM.iloc[start_index:end_index]

# Calculate rolling correlation of GE with the constant IBM window
roll_cor = GE.rolling(window=30).corr(ibm_window)

# Plotting the rolling correlation
plt.figure(figsize=(10, 5))
plt.plot(roll_cor, label='Rolling Correlation with IBM 1001-1030')
plt.title('Rolling Correlation between GE and IBM (Days 1001-1030)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
