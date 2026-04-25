
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create a DataFrame with stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing data and calculate returns
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix for compatibility

# Plot the results
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(loc='best')
plt.show()
