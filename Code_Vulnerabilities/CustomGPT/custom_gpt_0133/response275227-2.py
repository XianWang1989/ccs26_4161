
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Sample stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch adjusted closing prices
px = pd.DataFrame({n: get_px(n, '2009-01-01', '2012-06-01') for n in names})

# Handle missing data
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the initial value
df2.iloc[0] = 1  # Use iloc instead of ix since ix is deprecated.

# Plotting
df2.plot()
plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()
