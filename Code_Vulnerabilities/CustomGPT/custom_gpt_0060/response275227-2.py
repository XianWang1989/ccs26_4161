
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Set the backend to TkAgg
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Note: Ensure to have 'pandas_datareader' installed: pip install pandas_datareader

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Update for latest pandas version

# Now plot the data
df2.plot()
plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()  # Ensure to call plt.show() to display the plot
