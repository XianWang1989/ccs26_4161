
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select the stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM
fixed_window_start = 1000
fixed_window_end = fixed_window_start + 30
fixed_ibm = IBM.iloc[fixed_window_start:fixed_window_end]

# Calculate rolling correlation with GE
rolling_cor = []

# Loop through every possible 30-day window in GE
for start in range(len(GE) - 30 + 1):
    window_ge = GE.iloc[start:start + 30]
    corr = fixed_ibm.corr(window_ge)  # Compute the correlation
    rolling_cor.append(corr)

# Convert the rolling correlations to a DataFrame
rolling_cor_df = pd.DataFrame(rolling_cor, index=GE.index[:len(rolling_cor)], columns=['Correlation'])

# Plot the results
plt.plot(rolling_cor_df)
plt.title('Rolling Correlation of Fixed IBM Window with GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
