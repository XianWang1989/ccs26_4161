
import matplotlib
matplotlib.use('TkAgg')  # Choose an appropriate backend

import pandas as pd
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create a DataFrame for adjusted prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Use iloc instead of ix, as ix is deprecated

# Plotting
df2.plot()
import matplotlib.pyplot as plt
plt.show()  # Ensure the plot is displayed
