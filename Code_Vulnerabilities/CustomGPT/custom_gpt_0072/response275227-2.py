
import matplotlib
matplotlib.use('Agg')  # Ensure a suitable backend
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix for modern pandas

df2.plot()
plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.savefig('stock_returns.png')  # Save the plot as a PNG file
plt.close()  # Close the plot
