
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the start and end of the constant window for IBM
start_date = '2018-06-01'
end_date = '2018-06-30'
constant_window_IBM = IBM[start_date:end_date]

# Prepare to store the rolling correlations
rolling_correlations = []

# Loop through each possible 30-day window in GE
window_size = 30
for i in range(len(GE) - window_size + 1):
    # Get the current 30-day window for GE
    current_window_GE = GE[i:i + window_size]
    # Calculate the correlation with the constant IBM window
    correlation = constant_window_IBM.corr(current_window_GE)
    rolling_correlations.append(correlation)

# Create a date range for the correlations
dates = GE.index[:len(rolling_correlations)]

# Plot the rolling correlations
plt.figure(figsize=(10, 5))
plt.plot(dates, rolling_correlations, label='Rolling Correlation with IBM (30-Day Constant Window)', color='blue')
plt.title('Rolling Correlation of GE with 30-Day Constant Window of IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.grid()
plt.show()
