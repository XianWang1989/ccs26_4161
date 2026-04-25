
import pandas as pd
import web  # Ensure you have the correct import for web
import matplotlib
matplotlib.use('TkAgg')  # Use a compatible backend for plotting

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create a DataFrame with stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the first value to 1
df2.iloc[0] = 1

# Plot the DataFrame
df2.plot(title='Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(names)
plt.show()  # Ensure to call plt.show() to display the plot
