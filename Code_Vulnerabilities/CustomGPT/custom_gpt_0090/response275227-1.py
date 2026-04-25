
import matplotlib
# Switch to a different backend
matplotlib.use('TkAgg')

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Update to iloc for better practice

# Plot
df2.plot()
plt.show()
