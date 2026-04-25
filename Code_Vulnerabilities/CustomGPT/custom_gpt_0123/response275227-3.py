
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Update the list of stock names as needed
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C'] 

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fillna method pad uses last valid observation to fill
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the initial value to 1
df2.iloc[0] = 1  # Changed from df2.ix[0] to df2.iloc[0]

# Plotting
plt.figure(figsize=(10, 6))
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()
