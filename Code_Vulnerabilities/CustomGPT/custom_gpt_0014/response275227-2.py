
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')  # Set the backend

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Retrieve and prepare stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set initial value
df2.iloc[0] = 1

# Plot the results
df2.plot(title='Cumulative Returns of Stocks', xlabel='Date', ylabel='Cumulative Returns')
plt.show()
