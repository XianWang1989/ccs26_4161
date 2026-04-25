
import pandas as pd
import numpy as np
import matplotlib
# Set the backend
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Define stock names and function
names = ['AAPL','MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1

# Plotting
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.ylabel('Cumulative Returns')
plt.xlabel('Date')
plt.grid()
plt.show()
