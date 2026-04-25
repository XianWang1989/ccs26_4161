
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Fixed window for IBM
fixed_window_start = 1000  # Starting index for the fixed window
fixed_window_end = fixed_window_start + 30  # Ending index for the fixed window
fixed_IBM = IBM[fixed_window_start:fixed_window_end]

# Calculate rolling correlation with GE for every possible 30-day window
roll_cor = []
for start in range(len(GE) - 30 + 1):
    end = start + 30
    current_GE = GE[start:end]
    correlation = np.corrcoef(fixed_IBM, current_GE)[0, 1]
    roll_cor.append(correlation)

# Plotting the relationship
plt.plot(range(len(roll_cor)), roll_cor)
plt.title('Rolling Correlation between Fixed IBM Window and GE')
plt.xlabel('GE 30-Day Window Start Index')
plt.ylabel('Correlation')
plt.show()
