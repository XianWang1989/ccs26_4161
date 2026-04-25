
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Change backend if necessary
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set starting point
df2.iloc[0] = 1

# Plot
df2.plot()
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend(names)
plt.show()
