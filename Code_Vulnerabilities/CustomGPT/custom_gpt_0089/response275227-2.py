
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Set the plotting backend
%matplotlib inline

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Add other stocks as needed

def get_px(stock, start, end):
    return web.DataReader(stock, 'yahoo', start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '2009-01-01', '2012-06-01') for n in names})

# Fill NaN values using method pad
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix, which is deprecated

df2.plot(title='Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(loc='best')
plt.show()
