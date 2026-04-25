
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Set the backend
import matplotlib
matplotlib.use('Qt5Agg')  # or 'TkAgg'

# Stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create a DataFrame with adjusted closing prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing data
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set initial value
df2.ix[0] = 1

# Plot the data
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.grid()
plt.legend(names)
plt.show()  # Display the plot
