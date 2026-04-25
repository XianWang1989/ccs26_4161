
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Use a different backend explicitly
plt.switch_backend('Qt5Agg')

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fillna method pad uses last valid observation to fill
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.ix[0] = 1

# Plotting
df2.plot()
plt.show()  # Ensure the plot is shown
