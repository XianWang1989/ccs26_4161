
import matplotlib
# Set the backend to a different option like 'TkAgg'
matplotlib.use('TkAgg')

import pandas as pd
import pandas_datareader.data as web  # Make sure you have this library
import matplotlib.pyplot as plt

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '2009-01-01', '2012-06-01') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use 'iloc' instead of 'ix' for compatibility with newer pandas

df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()
