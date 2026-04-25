
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Set the matplotlib backend if necessary
# For a script, you might want to uncomment the next line:
# plt.switch_backend('TkAgg')

# List of stock names
names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']

# Function to get stock prices
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create a DataFrame with adjusted closing prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values by forward-filling
px = px.asfreq('B').fillna(method='pad')

# Calculate returns
rets = px.pct_change()
df2 = (1 + rets).cumprod() - 1

# Make sure to set the initial value for the first date
df2.iloc[0] = 1  # Use iloc for positional indexing

# Plot the data
df2.plot()
plt.title('Stock Returns Over Time')  # Adding a title
plt.xlabel('Date')  # Adding x-label
plt.ylabel('Cumulative Returns')  # Adding y-label
plt.grid()  # Adding a grid
plt.show()  # Ensure that the plot is displayed in the notebook or script
