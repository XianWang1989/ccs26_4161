
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Set the backend

import matplotlib.pyplot as plt
import pandas_datareader.data as web  # Make sure you have this import

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Adjusted stock list

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Get adjusted close prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Correcting the row assignment

# Plot the data
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend(title='Stocks')
plt.show()  # Ensure the plot is shown
