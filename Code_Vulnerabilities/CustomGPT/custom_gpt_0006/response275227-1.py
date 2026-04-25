
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader.data as web

# Change the backend if needed
# Uncomment the following line to specify a GUI backend
# import matplotlib
# matplotlib.use('TkAgg')  # or 'Qt5Agg', depending on what you have

# Stocks to analyze
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Getting stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set initial value
df2.iloc[0] = 1

# Plotting
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(loc='best')
plt.grid()
plt.show()  # Ensure the plot shows up in your environment
