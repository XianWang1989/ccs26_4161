
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Switch to a different backend
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch stock data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the first entry to 1
df2.iloc[0] = 1

# Plot the results
df2.plot()
plt.title("Cumulative Returns of Stocks")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.legend(names)
plt.show()
