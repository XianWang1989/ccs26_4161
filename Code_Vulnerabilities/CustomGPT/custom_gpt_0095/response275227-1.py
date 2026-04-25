
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Set the matplotlib backend
plt.switch_backend('Qt5Agg')  # Replace 'Qt5Agg' with 'TkAgg' or another backend if you have issues.

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Adjusted stock names
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch stock prices
px = pd.DataFrame({n: get_px(n, '2009-01-01', '2012-06-01') for n in names})

# Resample and fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Ensure the first row is set to 1
df2.iloc[0] = 1

# Plot the data
df2.plot(title='Cumulative Returns of Stocks', ylabel='Cumulative Return')
plt.show()
