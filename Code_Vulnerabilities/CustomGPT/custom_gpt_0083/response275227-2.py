
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg or Qt5Agg based on your system

import matplotlib.pyplot as plt
import pandas_datareader.data as web  # Make sure to import the right data reader

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN values using the last valid observation
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Adjusting the first row of df2

df2.plot()
plt.show()  # Make sure to call plt.show() to display the plot
