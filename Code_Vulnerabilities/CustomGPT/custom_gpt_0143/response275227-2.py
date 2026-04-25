
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as web  # Ensure you have yfinance installed

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.download(stock, start=start, end=end)['Adj Close']

px = pd.DataFrame({n: get_px(n, '2009-01-01', '2012-06-01') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = (1 + rets).cumprod() - 1

# Set the initial value to 1
df2.iloc[0] = 1

# Plotting
plt.figure(figsize=(10, 5))
df2.plot()
plt.title("Cumulative Returns of Selected Stocks")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.grid()
plt.show()
