
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web  # Make sure to have this library installed

# Set the matplotlib backend for interactive plotting if needed
# Uncomment the line below if you run this in a Jupyter notebook
# %matplotlib inline

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Ensure all stocks are valid
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill NaN values using the last valid observation for each column
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.ix[0] = 1  # Set the first index to 1 for cumulative returns

# Plotting the figure
df2.plot()  # Create the plot
plt.show()  # Show the plot explicitly
