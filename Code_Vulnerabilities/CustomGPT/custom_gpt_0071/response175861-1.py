
import pandas as pd
import matplotlib.pyplot as plt

# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for IBM
start_index = 1001
end_index = start_index + 30

# Select the fixed window for IBM
fixed_ibm_window = IBM[start_index:end_index]

# Store the rolling correlations
rolling_correlations = []

# Loop through every possible 30-day window of GE
for start in range(len(GE) - 30 + 1):
    end = start + 30
    ge_window = GE[start:end]
    correlation = fixed_ibm_window.corr(ge_window)
    rolling_correlations.append(correlation)

# Create a DataFrame for the correlations with the corresponding dates
dates = GE.index[:len(rolling_correlations)]
correlation_df = pd.DataFrame(rolling_correlations, index=dates, columns=['Correlation'])

# Plot the correlations
plt.plot(correlation_df)
plt.title('Rolling Correlation between IBM (fixed) and GE')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
