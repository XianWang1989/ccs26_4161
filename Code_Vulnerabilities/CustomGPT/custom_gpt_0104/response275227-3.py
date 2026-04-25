
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import datetime

# Set the matplotlib inline if in Jupyter Notebook
# %matplotlib inline

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get stock prices
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Initialize the first row
df2.iloc[0] = 0  # Fix to 0, previously it was 1

# Plot the results
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend(names)
plt.show()
