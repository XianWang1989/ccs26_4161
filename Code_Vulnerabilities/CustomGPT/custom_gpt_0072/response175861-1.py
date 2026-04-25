
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (days 1001-1030)
start_date = '1001-01-01'  # Replace with actual start date
end_date = '1001-01-30'    # Replace with actual end date
fixed_window_GE = GE.loc[start_date:end_date]

# Calculate rolling correlation with IBM
roll_cor = IBM.rolling(window=30).corr(fixed_window_GE)

# Plotting
plt.plot(roll_cor)
plt.title('Rolling Correlation of IBM with Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
