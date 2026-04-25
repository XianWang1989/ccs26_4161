
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE
fixed_start = 1000  # Adjust this as needed for your data
fixed_end = fixed_start + 30

# Calculate rolling correlations
rolling_correlations = []

for start in range(len(IBM) - 30):
    end = start + 30
    # Calculate and store the correlation
    correlation = GE[start:end].corr(IBM[fixed_start:fixed_end])
    rolling_correlations.append(correlation)

# Create a DataFrame for the results
rolling_cor_df = pd.DataFrame(rolling_correlations, index=pd.date_range(start=Stocks.index[0], periods=len(rolling_correlations), freq='D')[:-30], columns=['Correlation'])

# Plot the result
plt.plot(rolling_cor_df)
plt.title('Rolling Correlation between GE and Fixed IBM window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
