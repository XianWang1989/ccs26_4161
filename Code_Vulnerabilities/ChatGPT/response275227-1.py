
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import web

# Sample stock data creation for demonstration purposes
dates = pd.date_range(start='1/1/2009', end='6/1/2012', freq='B')
num_stocks = len(['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C'])
# Create some random data to mimic stock prices
data = np.random.randn(len(dates), num_stocks).cumsum(axis=0)

# Create a DataFrame with random prices
px = pd.DataFrame(data, index=dates, columns=['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C'])

# Fillna method pad uses last valid observation to fill
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix for compatibility

# Plotting the data
df2.plot(figsize=(10, 6))
plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
