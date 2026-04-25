
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the start and end dates for the constant window
start_date = 'yyyy-mm-dd'  # Replace with the start date of your constant window (e.g., '2003-01-01')
end_date = 'yyyy-mm-dd'    # Replace with the end date of your constant window (e.g., '2003-01-30')

# Slice the GE stock prices for the constant window
GE_constant = GE[start_date:end_date]

# Calculate the rolling correlation with GE_constant
# Create a new DataFrame to hold the correlations
correlations = []
for i in range(len(IBM) - 30):
    IBM_window = IBM[i:i + 30]  # Get the current 30-day window of IBM
    corr = GE_constant.corr(IBM_window)  # Calculate correlation with the GE constant window
    correlations.append(corr)

# Create a series for the correlations with a proper date index
correlation_series = pd.Series(correlations, index=IBM.index[0:len(correlations)])

# Plot the correlation
plt.figure(figsize=(10, 6))
plt.plot(correlation_series)
plt.title('Rolling Correlation between GE (constant window) and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Add a horizontal line at y=0
plt.grid()
plt.show()
