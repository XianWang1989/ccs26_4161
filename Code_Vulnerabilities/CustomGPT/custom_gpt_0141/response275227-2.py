
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web  # Ensure this is in your environment

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Stocks to analyze

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Fetch stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing data
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Set the initial value to 1

# Create a plot
fig, ax = plt.subplots()
df2.plot(ax=ax)  # Specify axis
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.grid()
plt.show()  # Ensure the plot is shown
