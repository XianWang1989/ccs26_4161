
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web  # Make sure you have this package installed

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.DataReader(stock, 'yahoo', start, end)['Adj Close']

# Set the time period for fetching data
start_date = '2009-01-01'
end_date = '2012-06-01'

px = pd.DataFrame({n: get_px(n, start_date, end_date) for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix for compatibility

# Change the backend for matplotlib
import matplotlib
matplotlib.use('TkAgg')  # Change as needed

# Now plot the data
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.grid()
plt.legend(loc='best')
plt.show()
