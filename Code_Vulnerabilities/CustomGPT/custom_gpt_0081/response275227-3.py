
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Change to TkAgg or Qt5Agg backend before plotting
# Uncomment the line below if necessary
# import matplotlib
# matplotlib.use('TkAgg')  

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN values using the last valid observation
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Fix index with a valid initial value
df2.iloc[0] = 1

# Plotting
df2.plot()
plt.title('Cumulative Returns of Selected Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()
