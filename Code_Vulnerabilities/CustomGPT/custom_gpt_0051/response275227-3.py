
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Ensure you set the Matplotlib backend
%matplotlib inline

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C'] 

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Gather data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Fix the first element
df2.iloc[0] = 1

# Plot the data
df2.plot()
plt.title("Cumulative Returns of Stocks")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.legend(names)
plt.show()
