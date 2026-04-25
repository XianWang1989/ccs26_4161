
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Set the backend
%matplotlib inline  # Use this in Jupyter Notebook

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NA values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Setting the first value to 1
df2.iloc[0] = 1

# Plotting
df2.plot(title='Stock Returns')
plt.ylabel('Cumulative Return')
plt.xlabel('Date')
plt.show()
