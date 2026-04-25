
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Define the fixed window dates for GE
start_date = '2020-01-01'
end_date = '2020-01-30'
GE_window = Stocks['GE'][start_date:end_date]

# Initialize a list to store correlation results
correlations = []

# Loop over possible starting points for IBM's 30-day windows
for i in range(len(Stocks) - 30 + 1):
    IBM_window = Stocks['IBM'].iloc[i:i + 30]
    correlation = GE_window.corr(IBM_window)
    correlations.append((Stocks.index[i], correlation))

# Convert results to a DataFrame
correlation_df = pd.DataFrame(correlations, columns=['Date', 'Correlation'])
correlation_df.set_index('Date', inplace=True)

# Plot the correlations
plt.plot(correlation_df.index, correlation_df['Correlation'])
plt.title('Rolling Correlation between GE and IBM (Fixed GE Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
