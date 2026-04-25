
import pandas as pd
import matplotlib
# Change backend if necessary
matplotlib.use('Qt5Agg')  # or 'TkAgg'
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get prices
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create DataFrame of adjusted close prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set initial value for the first entry
df2.iloc[0] = 1

# Plot the results
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend(title='Stocks')
plt.show()
