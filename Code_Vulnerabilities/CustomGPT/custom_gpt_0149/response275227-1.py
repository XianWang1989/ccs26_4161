
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get stock prices
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create DataFrame with adjusted close prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

# Calculate returns and cumulative returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Use .iloc for index-based assignment

# Plotting the returns
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.ylabel('Cumulative Returns')
plt.xlabel('Date')
plt.legend(loc='best')
plt.grid()
plt.show()
