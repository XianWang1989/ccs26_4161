
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

names = ['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C']  # Ensure this list is valid
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

# Create a DataFrame with adjusted closing prices
px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

# Fill missing values
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
df2 = (1 + rets).cumprod() - 1

# Set the first row to 1
df2.iloc[0] = 1

# Plotting
plt.figure(figsize=(10, 6))  # Set figure size
df2.plot()  # Plot the data
plt.title('Cumulative Returns of Stocks')  # Add a title
plt.xlabel('Date')  # Label x-axis
plt.ylabel('Cumulative Return')  # Label y-axis
plt.legend(names)  # Add legend
plt.grid(True)  # Enable grid
plt.show()  # Display the plot
