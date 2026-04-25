
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Ensure to set the backend
plt.switch_backend('TkAgg')  # or another suitable backend

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get stock data
def get_px(stock, start, end):
    return web.DataReader(stock, 'yahoo', start, end)['Adj Close']

# Retrieve and preprocess data
px = pd.DataFrame({n: get_px(n, '2009-01-01', '2012-06-01') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # Use iloc instead of ix for compatibility

# Plotting
df2.plot()
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()
