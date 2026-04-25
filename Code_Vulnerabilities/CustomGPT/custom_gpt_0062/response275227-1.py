
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Set the backend for Jupyter
%matplotlib inline

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Downloading the data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NA values and calculate returns
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the initial value for the first row
df2.iloc[0] = 1

# Plotting
df2.plot(title='Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend(title='Stocks')
plt.show()
