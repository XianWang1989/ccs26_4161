
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime

# Define stock tickers
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Adjusted for valid tickers

# Function to get stock prices
def get_px(stock, start, end):
    return web.DataReader(stock, 'yahoo', start, end)['Adj Close']

# Date range
start = datetime.datetime(2009, 1, 1)
end = datetime.datetime(2012, 6, 1)

# Collect data into a DataFrame
px = pd.DataFrame({n: get_px(n, start, end) for n in names})

# Fill missing data
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Ensure initial value is 1
df2.iloc[0] = 1

# Plotting
df2.plot()
plt.title('Cumulative Returns')
plt.ylabel('Cumulative Return')
plt.xlabel('Date')
plt.show()
