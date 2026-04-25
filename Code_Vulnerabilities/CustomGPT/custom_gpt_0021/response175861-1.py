
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window
start_date = 1001
end_date = start_date + 29  # 30 days window

# Slice the constant window for GE
constant_window_GE = GE.iloc[start_date:end_date]

# Create a list to store correlations
correlations = []

# Calculate rolling correlation for each window of IBM
for start in range(len(IBM) - 30 + 1):
    rolling_window_IBM = IBM.iloc[start:start + 30]
    corr = constant_window_GE.corr(rolling_window_IBM)
    correlations.append(corr)

# Create a DataFrame for the correlations
corr_df = pd.DataFrame(correlations, index=IBM.index[:len(correlations)])

# Plot the rolling correlations
plt.figure(figsize=(14, 7))
plt.plot(corr_df)
plt.title('Rolling Correlation between Constant GE Window and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
