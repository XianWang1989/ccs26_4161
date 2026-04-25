
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Ensure we plot inline if using Jupyter Notebook
%matplotlib inline

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values using the last valid observation
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Initialize the first row
df2.loc[df2.index[0]] = 1

# Plot the data
df2.plot(title="Stock Returns")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.show()
