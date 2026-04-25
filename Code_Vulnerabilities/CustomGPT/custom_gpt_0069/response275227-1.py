
import pandas as pd
import matplotlib.pyplot as plt
import web   # Make sure to import your data fetching library

# Set matplotlib to use a different backend
plt.switch_backend('TkAgg')  # Change to 'Qt5Agg' if using Qt

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN values using the last valid observation
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix, as ix is deprecated

# Plot the data
df2.plot()
plt.title('Stock Returns from 2009 to 2012')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(loc='best')
plt.show()
