
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Set the matplotlib backend for Jupyter
%matplotlib inline

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Construct DataFrame of stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values using forward fill
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = (1 + rets).cumprod() - 1
df2.iloc[0] = 1  # Set the first value to 1

# Plot the results
df2.plot()
plt.title('Stock Returns from 2009 to 2012')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.show()
