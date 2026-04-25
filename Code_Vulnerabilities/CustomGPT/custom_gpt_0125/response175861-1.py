
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices into a DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM
fixed_window_start = 1000  # Starting at index 1000 for IBM
fixed_window_end = fixed_window_start + 30  # 30-day window

# Extract the fixed window for IBM
fixed_ibm_window = IBM.iloc[fixed_window_start:fixed_window_end]

# Create a list to store rolling correlations
rolling_correlations = []

# Calculate correlation for every possible 30-day window in GE
for start in range(len(GE) - 29):  # Adjust the range accordingly
    ge_window = GE.iloc[start:start + 30]
    correlation = fixed_ibm_window.corr(ge_window)
    rolling_correlations.append(correlation)

# Create a DataFrame for the rolling correlations
roll_cor_df = pd.DataFrame(rolling_correlations, index=GE.index[:len(rolling_correlations)], columns=['Correlation'])

# Plotting the rolling correlation
plt.figure(figsize=(12, 6))
plt.plot(roll_cor_df, label='Rolling Correlation (IBM Fixed vs GE)')
plt.title('Rolling Correlation of Fixed IBM Window with GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
