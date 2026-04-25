
import pandas as pd
import matplotlib
# Switch to Agg backend for non-interactive plotting
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Stock symbols
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch data and create DataFrame
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set initial index value
df2.iloc[0] = 1

# Plotting
df2.plot()
plt.title('Cumulative Returns for Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.savefig('cumulative_returns.png')  # Save figure to a file
plt.close()  # Close the plot to avoid display
