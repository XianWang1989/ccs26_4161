
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Switch to an interactive backend for this script if needed
# Uncomment the following line if running in a script
# plt.switch_backend('TkAgg')  # or 'Qt5Agg' depending on your environment

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')

rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Use iloc instead of ix (deprecated)

# Plotting
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid()
plt.show()
