
import matplotlib
matplotlib.use('TkAgg') # Set the backend to TkAgg
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

# List of stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get stock prices
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Retrieve prices and create DataFrame
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing data
px = px.asfreq('B').fillna(method='pad')

# Calculate returns and cumulative returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Set the first value to 1

# Plot the cumulative returns
df2.plot(title='Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()
