
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import web

# Set the backend to a compatible one
matplotlib.use('TkAgg')  # You may also try 'Qt5Agg' or others based on your setup

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Add more stocks as needed

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN values using forward fill method
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Ensure the first row is set to 1 for proper cumulative returns
df2.iloc[0] = 1  # Use iloc instead of ix as ix is deprecated

# Plotting the DataFrame
df2.plot()
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()
