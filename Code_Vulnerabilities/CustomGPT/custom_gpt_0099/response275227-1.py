
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Set the backend (choose a stable one)
matplotlib.use('TkAgg')  # or 'Qt5Agg', depending on your installation

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create a DataFrame with adjusted close prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fillna method pad uses last valid observation to fill
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the first value to 1
df2.iloc[0] = 1

# Plot the data
df2.plot()
plt.title('Stock Returns Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()  # This ensures the plot is displayed correctly
