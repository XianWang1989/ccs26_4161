
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# Set the Matplotlib backend
plt.switch_backend('Agg')  # Use 'Agg' for script-based settings

# Define stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get stock data
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Get stock prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = ((1 + rets).cumprod() - 1)

# Set the first entry to 1
df2.iloc[0] = 1

# Plot the results
df2.plot()
plt.title('Cumulative Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid()
plt.savefig('stocks_plot.png')  # Save the plot as an image
plt.show()  # Show the plot if in an interactive environment
