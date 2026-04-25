
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Uncomment and set the backend if running interactively:
# import matplotlib
# matplotlib.use('TkAgg')  # For Windows/Linux, or 'MacOSX' for macOS

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # goog and SF did not work

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

df2.iloc[0] = 1  # Use iloc instead of ix, as ix is deprecated

df2.plot(title='Stock Returns Over Time')  # Optional: Adding title for clarity
plt.ylabel('Cumulative Returns')  # Optional: Label y-axis
plt.show()  # Show the plot
