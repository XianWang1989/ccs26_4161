
import matplotlib
matplotlib.use('Agg')  # Switch to a non-interactive backend
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Adjust your stock names as necessary
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)
df2.iloc[0] = 1  # corrected the warning for .ix usage

# Now use plt.plot instead of df2.plot() for more control
plt.figure(figsize=(10, 6))
for column in df2.columns:
    plt.plot(df2.index, df2[column], label=column)

plt.legend()
plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.grid()
plt.show()
