
import matplotlib
matplotlib.use('Agg')  # Switch to a non-interactive backend
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # stock symbols

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fillna method pad uses last valid observation to fill
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the initial value
df2.iloc[0] = 1

# Plot
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.savefig('cumulative_returns.png')  # Save the plot as an image
