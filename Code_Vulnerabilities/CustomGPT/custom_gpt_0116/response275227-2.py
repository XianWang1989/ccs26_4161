
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Stocks list
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get adjusted close prices
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create DataFrame
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Fix the starting point

# Plotting
df2.plot()
plt.title('Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.grid()
plt.show()
