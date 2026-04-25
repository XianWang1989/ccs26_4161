
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the constant window for IBM (e.g., days 1001-1030)
start_date = '1001-01-01'  # Adjust this date based on your dataset
end_date = '1001-01-30'    # Adjust this date based on your dataset

# Select the 30-day window for IBM
ibm_window = IBM[start_date:end_date]

# Prepare to store the rolling correlations
rolling_cor = []

# Iterate through all possible 30-day windows of GE
for i in range(len(GE) - 30 + 1):
    ge_window = GE[i:i + 30]
    correlation = ibm_window.corr(ge_window)
    rolling_cor.append(correlation)

# Create a series with the correlational data
rolling_cor_series = pd.Series(rolling_cor, index=GE.index[29:])

# Plot the results
plt.plot(rolling_cor_series)
plt.title('Rolling Correlation between GE and IBM (Fixed Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
