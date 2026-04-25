
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Retrieve stock data
px = pd.DataFrame({n: get_px(n, '2009-01-01', '2012-06-01') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use .iloc instead of .ix since .ix is deprecated

# Plotting
df2.plot(title='Cumulative Returns', xlabel='Date', ylabel='Cumulative Return')
plt.show()
