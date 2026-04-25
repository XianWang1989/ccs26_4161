
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Include only valid stocks

def get_px(stock, start, end):
    return web.DataReader(stock, 'yahoo', start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '2009-01-01', '2012-06-01') for n in names})

# Fill NaN values with the last valid observation
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix for compatibility

plt.figure(figsize=(10, 6))  # Set figure size
df2.plot(title='Stock Returns')  # Add a title
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.grid()  # Add a grid
plt.legend(loc='best')  # Add a legend
plt.show()  # Ensure the plot displays
