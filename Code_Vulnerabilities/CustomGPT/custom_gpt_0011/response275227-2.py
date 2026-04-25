
import matplotlib
matplotlib.use('TkAgg')  # Ensure you use a suitable interactive backend
import pandas as pd
import pandas_datareader.data as web  # Make sure you have imported the necessary module

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN values using the last valid observation to fill
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix for compatibility with the latest versions of pandas

# Plotting
df2.plot()
import matplotlib.pyplot as plt
plt.show()  # Use plt.show() to display the plot
