
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create DataFrame from the stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set first row to 1
df2.iloc[0] = 1

# Plotting
df2.plot()
plt.title('Cumulative Returns of Various Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()  # Use plt.show() to display the plot
