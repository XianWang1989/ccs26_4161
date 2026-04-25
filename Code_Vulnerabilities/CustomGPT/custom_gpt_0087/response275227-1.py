
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get stock prices
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create DataFrame with adjusted close prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the first row value
df2.iloc[0] = 1

# Plotting
plt.figure(figsize=(10, 6))
df2.plot()
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.grid()
plt.show()
