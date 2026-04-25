
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
import matplotlib.pyplot as plt
import pandas_datareader.data as web  # Ensure you have the correct import

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Note: using iloc instead of ix for compatibility

df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.ylabel('Cumulative Returns')
plt.xlabel('Dates')
plt.show()  # Use plt.show() to display the plot
