
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get adjusted close prices
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Get stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the initial value
df2.iloc[0] = 1

# Create the figure and axis
fig, ax = plt.subplots()
df2.plot(ax=ax)

# Show the plot
plt.show()
