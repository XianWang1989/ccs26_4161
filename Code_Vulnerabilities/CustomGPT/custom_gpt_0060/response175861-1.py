
import pandas as pd
import matplotlib.pyplot as plt

# Read the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for IBM
start_day = 1000  # Change to the appropriate index for your DataFrame
end_day = start_day + 30

# Slice the IBM prices for the constant window
constant_window_ibm = IBM[start_day:end_day]

# Initialize a list to store correlation results
correlations = []

# Compute rolling correlation of GE for every possible 30-day window
for start in range(len(GE) - 30):
    end = start + 30
    rolling_window_ge = GE[start:end]

    # Calculate correlation between the constant IBM window and the current GE window
    correlation = constant_window_ibm.corr(rolling_window_ge)
    correlations.append(correlation)

# Create a DataFrame for the correlations with the proper index
correlation_index = GE.index[30:]  # Adjust index to match the number of correlation results
correlation_series = pd.Series(correlations, index=correlation_index)

# Plotting the correlations
plt.figure(figsize=(10, 5))
plt.plot(correlation_series, label='Rolling Correlation with IBM (Days 1001-1030)', color='blue')
plt.title('Rolling Correlation between IBM (Fixed Window) and GE (Variable Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.show()
