
import matplotlib
matplotlib.use('TkAgg')  # Change this to 'Qt5Agg' if preferred
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

# Your stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C'] 

# Function to get adjusted close price data
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create DataFrame from stock data
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()

# Compute cumulative returns
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Set the first value

# Plotting the data
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()
