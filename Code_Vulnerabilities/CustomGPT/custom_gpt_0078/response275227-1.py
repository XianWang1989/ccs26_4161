
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Change the backend (If using Jupyter, put this line at the top)
# %matplotlib inline  # Use this for Jupyter

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Retrieve stock price data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing data
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = (1 + rets).cumprod() - 1

# Set initial value
df2.iloc[0] = 1

# Plotting the data
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.grid()
plt.show()
