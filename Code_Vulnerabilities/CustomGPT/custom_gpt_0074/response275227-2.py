
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Change the backend before importing pyplot
import matplotlib.pyplot as plt
import pandas_datareader.data as web  # Make sure to install this package

names = ['AAPL','MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch stock data into a DataFrame
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Fix the index for plotting
df2.iloc[0] = 1

# Plotting
df2.plot()

# Save the plot to a file instead of showing it
plt.savefig('stock_returns.png')
