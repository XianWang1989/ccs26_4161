
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM (days 1001 to 1030)
fixed_window_start = 1000  # Adjust based on your index
fixed_window_end = fixed_window_start + 30

# Get the fixed window data for IBM
fixed_IBM_window = IBM.iloc[fixed_window_start:fixed_window_end]

# List to store correlation values
corr_values = []

# Loop through the possible 30-day windows in GE
for start in range(len(GE) - 30 + 1):
    end = start + 30
    window_GE = GE.iloc[start:end]
    correlation = fixed_IBM_window.corr(window_GE)
    corr_values.append(correlation)

# Create a DataFrame for the correlation results
correlation_df = pd.DataFrame(corr_values, columns=['Correlation'])

# Plot the correlation values
plt.plot(correlation_df)
plt.title('Correlation of Fixed IBM Window with Rolling GE Windows')
plt.xlabel('Rolling Window Start Index')
plt.ylabel('Correlation')
plt.show()
