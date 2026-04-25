
import pandas as pd
import matplotlib.pyplot as plt

# Load your stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for IBM
fixed_window_start = 1000  # Adjust based on your data
fixed_window_end = fixed_window_start + 30
fixed_ibm_window = IBM.iloc[fixed_window_start:fixed_window_end]

# Prepare to store correlation results
corr_results = []

# Loop through GE to compute the correlation with the fixed IBM window
for start in range(len(GE) - 29):  # 29 to account for the end index
    ge_window = GE.iloc[start:start + 30]
    correlation = fixed_ibm_window.corr(ge_window)
    corr_results.append(correlation)

# Convert to a Pandas Series for easier plotting
rolling_cor = pd.Series(corr_results, index=GE.index[:len(corr_results)])

# Plot the correlation results
plt.figure(figsize=(10, 6))
plt.plot(rolling_cor, label='Rolling Correlation with Fixed IBM Window')
plt.title('Rolling Correlation: Fixed IBM Window vs GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
