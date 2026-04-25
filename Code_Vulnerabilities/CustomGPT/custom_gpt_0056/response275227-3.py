
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Set the backend for matplotlib (if needed)
# matplotlib.use('TkAgg')  # Uncomment if needed

# Ensure plots are shown inline in Jupyter Notebook
%matplotlib inline  

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values and calculate returns
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = (1 + rets).cumprod() - 1

df2.iloc[0] = 1  # Use iloc instead of ix for recent versions

# Plot the cumulative returns
df2.plot(title='Cumulative Returns of Stocks', ylabel='Cumulative Return')
plt.show()
