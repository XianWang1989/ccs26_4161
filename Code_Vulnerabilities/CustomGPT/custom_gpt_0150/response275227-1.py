
import matplotlib
matplotlib.use('TkAgg')  # Change to a compatible backend like TkAgg or Qt5Agg

import pandas as pd
import numpy as np
import pandas_datareader.data as web

names = ['AAPL','MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fillna method pad uses the last valid observation to fill
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix, as ix is deprecated

df2.plot()
import matplotlib.pyplot as plt
plt.show()  # Ensure the plot displays
