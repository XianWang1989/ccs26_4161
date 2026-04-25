
import pandas as pd
import matplotlib
# Set the backend
matplotlib.use('TkAgg')  # or 'Qt5Agg'
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NA values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Ensure to set index correctly in case the index has shifted
df2.iloc[0] = 1  # Using iloc to avoid deprecated .ix

# Plot the data
df2.plot(title='Stock Returns', figsize=(10, 5))
plt.ylabel('Cumulative Returns')
plt.grid()
plt.show()
