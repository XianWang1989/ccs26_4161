
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Switch to an interactive backend, if necessary.
plt.switch_backend('TkAgg')

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.DataReader(stock, 'yahoo', start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '2009-01-01', '2012-06-01') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.loc[df2.index[0]] = 1  # Update the first element

# Plotting
df2.plot(title='Cumulative Returns', grid=True)
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend(loc='best')
plt.show()
