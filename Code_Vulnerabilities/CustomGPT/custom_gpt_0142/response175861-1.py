
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the constant 30-day window for IBM (e.g., from day 1001 to day 1030)
start_day = 1000  # Adjust based on your DataFrame index
end_day = start_day + 30
constant_IBM_window = IBM.iloc[start_day:end_day]

# Create a list to store the rolling correlations
rolling_correlations = []

# Compute rolling correlations with the GE stock
for start in range(len(GE) - 30 + 1):
    ge_window = GE.iloc[start:start+30]
    corr = constant_IBM_window.corr(ge_window)
    rolling_correlations.append(corr)

# Convert the rolling correlations list to a DataFrame
rolling_cor_df = pd.DataFrame(rolling_correlations, index=GE.index[:len(rolling_correlations)], columns=['Correlation'])

# Plot the rolling correlations
plt.plot(rolling_cor_df)
plt.title('Rolling Correlation between Constant IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
