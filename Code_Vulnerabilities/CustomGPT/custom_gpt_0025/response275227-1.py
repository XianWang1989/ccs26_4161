
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader.data as web

# Change backend to TkAgg
import matplotlib
matplotlib.use('TkAgg')

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get stock data
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch stock prices
start_date = '2009-01-01'
end_date = '2012-06-01'
px = pd.DataFrame({n: get_px(n, start_date, end_date) for n in names})

# Fill missing data
px = px.asfreq('B').fillna(method='pad')

# Calculate returns and cumulative returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Set initial value to 1

# Plot cumulative returns
df2.plot(title='Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(loc='best')
plt.show()
