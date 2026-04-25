
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Set the backend
matplotlib.use('Agg')

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Stocks to fetch

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch and preprocess the data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')  # Fill NaN values
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Use iloc instead of ix

# Plotting
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend(loc='best')
plt.savefig('cumulative_returns.png')  # Save the plot as an image
