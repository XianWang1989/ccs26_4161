
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE
start = 1000  # Adjust based on your data
constant_window = GE[start:start+30]

# Initialize a list to store the correlations
correlations = []

# Loop through possible windows for IBM
for i in range(len(IBM) - 30):
    window = IBM[i:i+30]
    corr = constant_window.corr(window)
    correlations.append(corr)

# Create a Series for correlations with the proper index
correlation_series = pd.Series(correlations, index=IBM.index[0:len(correlations)])

# Plotting the result
plt.plot(correlation_series)
plt.title('Rolling Correlation of Constant Window with IBM')
plt.xlabel('Date')
plt.ylabel('Correlation Coefficient')
plt.show()
