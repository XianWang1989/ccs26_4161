
import matplotlib
# Uncomment this line if using Jupyter Notebook
# %matplotlib inline
matplotlib.use('TkAgg')  # Change to a suitable backend like TkAgg

import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

names = ['AAPL','MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch the price data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaNs
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()

# Calculate cumulative returns
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Change ix to iloc for more current pandas

# Plotting
df2.plot(title='Cumulative Returns of Stocks', ylabel='Cumulative Returns')
plt.show()  # Ensure the plot is displayed
