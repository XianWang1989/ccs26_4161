
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Update for latest pandas version

# Now save the plot instead of showing it
df2.plot()
plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.savefig('stock_returns.png')  # Save the figure to a file
