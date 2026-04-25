
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# If you're not using Jupyter, uncomment the following line to switch to TkAgg:
# import matplotlib
# matplotlib.use('TkAgg')

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C'] 

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Updated to use iloc instead of ix, as ix is deprecated

# Plot the data
df2.plot()
plt.title("Cumulative Returns of Stocks")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend(loc='upper left')
plt.show()
