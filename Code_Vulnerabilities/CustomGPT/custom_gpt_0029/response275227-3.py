
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Use a suitable backend for plotting
import matplotlib
matplotlib.use('TkAgg')

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NA values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Use .loc instead of .ix
df2.loc[0] = 1

# Plotting
df2.plot()
plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()
