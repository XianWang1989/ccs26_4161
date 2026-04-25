
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM
start = 1000  # starting index for IBM
end = start + 30  # end index for the 30-day window
fixed_window_IBM = IBM[start:end]

# Calculate rolling correlation with GE
rolling_cor = []

# Iterate through all possible 30-day windows in GE
for i in range(len(GE) - 30 + 1):
    rolling_window_GE = GE[i:i + 30]
    corr = fixed_window_IBM.corr(rolling_window_GE)
    rolling_cor.append(corr)

# Create a DataFrame to hold the correlation results
correlation_results = pd.DataFrame(rolling_cor, index=GE.index[:len(rolling_cor)], columns=['Correlation'])

# Plotting the rolling correlation
plt.plot(correlation_results)
plt.title('Rolling Correlation between Fixed IBM Window and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
