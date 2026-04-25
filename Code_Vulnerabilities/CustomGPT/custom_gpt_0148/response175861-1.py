
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Constant 30-day window for GE (example: days 1001 to 1030)
fixed_window_start = 1001
fixed_window_end = 1030
fixed_GE = GE.iloc[fixed_window_start:fixed_window_end]

# Calculate rolling correlations
roll_correlations = []
for i in range(len(IBM) - 29):  # Adjust for 30-day window
    rolling_window = IBM.iloc[i:i+30]
    correlation = np.corrcoef(fixed_GE, rolling_window)[0, 1]
    roll_correlations.append(correlation)

# Create a DataFrame for plotting
roll_cor_df = pd.DataFrame(roll_correlations, index=IBM.index[:len(roll_correlations)], columns=['Correlation'])

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(roll_cor_df, label='Rolling Correlation with Fixed GE Window', color='blue')
plt.axhline(0, color='black', lw=1, ls='--')
plt.title('Rolling Correlation between GE (fixed window) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
