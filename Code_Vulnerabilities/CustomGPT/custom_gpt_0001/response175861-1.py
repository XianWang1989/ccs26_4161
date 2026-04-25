
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (for example, days 1001-1030)
start_date = '2000-03-01'  # Example start date for the fixed window
end_date = '2000-03-30'    # Example end date for the fixed window
fixed_window_GE = GE[start_date:end_date]

# Create a DataFrame to store rolling correlations
rolling_correlations = []

# Calculate rolling correlations
for i in range(len(IBM) - 30 + 1):
    # Get the current 30-day window for IBM
    window_IBM = IBM[i:i+30]
    # Calculate the correlation and append to the list
    correlation = window_IBM.corr(fixed_window_GE)
    rolling_correlations.append(correlation)

# Create a Series for the rolling correlations for plotting
date_index = IBM.index[0:len(rolling_correlations)]
rolling_cor_series = pd.Series(rolling_correlations, index=date_index)

# Plot the rolling correlations
plt.plot(rolling_cor_series)
plt.title('Rolling Correlation between GE (fixed window) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
