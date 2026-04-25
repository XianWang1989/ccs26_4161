
import matplotlib
matplotlib.use('TkAgg')  # Use an interactive backend
import pandas as pd
import pandas_datareader.data as web

# Stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create DataFrame and fill missing values
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Ensure the first value is set to 1

# Plotting
df2.plot()
