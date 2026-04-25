
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Set a different backend
plt.switch_backend('TkAgg')  # or 'Qt5Agg', depending on your setup

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN values with the last valid observation
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix for compatibility

df2.plot()
plt.show()  # Show the plot
