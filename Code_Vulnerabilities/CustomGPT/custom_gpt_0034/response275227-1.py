
import matplotlib
matplotlib.use('TkAgg')  # Or use 'Qt5Agg'
import pandas as pd
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch the stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the first value
df2.iloc[0] = 1

# Plotting
df2.plot()
import matplotlib.pyplot as plt
plt.show()
