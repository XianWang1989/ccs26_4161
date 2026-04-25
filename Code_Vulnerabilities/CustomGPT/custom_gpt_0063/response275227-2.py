
import pandas as pd
import pandas_datareader.data as web
import matplotlib
matplotlib.use('TkAgg')  # Change this to 'Qt5Agg' if needed
import matplotlib.pyplot as plt

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Fix first row
df2.iloc[0] = 1

# Plotting
df2.plot()
plt.show()  # Ensure the plot displays correctly
