
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Use a different backend if necessary
import matplotlib
matplotlib.use('TkAgg')  # Change to 'Agg' in non-interactive environments

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN with forward fill
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use .iloc instead of .ix for compatibility with current versions

df2.plot()
plt.show()  # Ensure to call plt.show() to display the plot
