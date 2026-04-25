
import matplotlib
matplotlib.use('TkAgg')  # Use a different backend
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web  # Assuming you are using this to fetch data

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# This line may be updated to 'iloc' since 'ix' is deprecated
df2.iloc[0] = 1 

# Make your plot
df2.plot()
plt.show()  # Add this to display the plot
