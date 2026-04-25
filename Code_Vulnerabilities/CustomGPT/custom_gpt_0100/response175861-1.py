
import pandas as pd
import matplotlib.pyplot as plt

# Load your data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for GE (for example, days 1001-1030)
start_date = '2001-01-01'  # Replace with your actual start date
end_date = '2001-01-30'    # Replace with your actual end date
fixed_ge_window = GE[start_date:end_date]

# Calculate rolling correlation between the fixed GE window and the rolling IBM window
rolling_corr_values = []

# Iterate through every possible window for IBM
for i in range(len(IBM) - 29):  # 30 data points means len - 29
    ibm_window = IBM[i:i + 30]
    corr = fixed_ge_window.corr(ibm_window)
    rolling_corr_values.append(corr)

# Create a series for correlation with date index
dates = IBM.index[29:]  # Align the dates for the rolling correlation
roll_corr_series = pd.Series(rolling_corr_values, index=dates)

# Plot the results
plt.plot(roll_corr_series)
plt.title('Rolling Correlation between Fixed GE Window and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation Coefficient')
plt.show()
