
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '01/01/2009', '06/01/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')

rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Use iloc instead of ix for newer pandas versions

df2.plot()
plt.show()  # Make sure to call plt.show() to display the plot
