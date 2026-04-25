
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Set the fixed window for GE
fixed_start = 1000  # Adjust this to the desired starting index
fixed_end = fixed_start + 30
fixed_GE_window = GE.iloc[fixed_start:fixed_end]

# Calculate rolling correlations
roll_cor = []
for start in range(len(IBM) - 30 + 1):
    current_IBM_window = IBM.iloc[start:start + 30]
    correlation = current_IBM_window.corr(fixed_GE_window)
    roll_cor.append(correlation)

# Convert to a DataFrame for better handling
roll_cor_df = pd.DataFrame(roll_cor, index=IBM.index[:len(roll_cor)], columns=['Correlation'])

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(roll_cor_df)
plt.title('Rolling Correlation of IBM with Fixed GE Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axvline(x=IBM.index[fixed_start], color='red', linestyle='--', label='Fixed GE Window Start')
plt.axvline(x=IBM.index[fixed_end - 1], color='red', linestyle='--', label='Fixed GE Window End')
plt.legend()
plt.show()
