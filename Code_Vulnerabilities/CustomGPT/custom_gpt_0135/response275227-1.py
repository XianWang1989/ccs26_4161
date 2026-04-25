
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader.data as web

# Switch backend
import matplotlib
matplotlib.use('TkAgg')  # Or 'Qt5Agg' if you prefer

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C'] 

# Fetch stock prices
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set initial value
df2.iloc[0] = 1

# Plot
df2.plot(title='Stock Returns', ylabel='Cumulative Return')
plt.show()
