
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Set the backend
matplotlib.use('TkAgg')  # Change to appropriate backend as needed
%matplotlib inline  # Only for Jupyter notebooks

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create a DataFrame
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set initial value
df2.iloc[0] = 1  # Use iloc instead of ix for recent pandas versions

# Plotting
df2.plot()
plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.grid()
plt.show()
