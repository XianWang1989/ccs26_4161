
import matplotlib
# Set the backend
matplotlib.use('TkAgg')  # You can also try 'Qt5Agg'
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web  # Ensure you have pandas_datareader installed

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Example stock names

def get_px(stock, start, end):
    return web.DataReader(stock, 'yahoo', start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix, as ix is deprecated

# Plotting
df2.plot()
plt.title("Cumulative Returns of Stocks")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.show()
