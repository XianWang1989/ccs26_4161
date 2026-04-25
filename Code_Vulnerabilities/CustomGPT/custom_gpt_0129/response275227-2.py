
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Make sure to set the matplotlib inline
%matplotlib inline

# Adjust 'names' to include any stocks you are interested in:
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Download the data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill in any missing values using forward fill
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Setting initial value
df2.iloc[0] = 1  # Use .iloc instead of .ix for newer versions of pandas

# Plot the data
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.ylabel('Cumulative Returns')
plt.xlabel('Date')
plt.legend(loc='best')
plt.show()
