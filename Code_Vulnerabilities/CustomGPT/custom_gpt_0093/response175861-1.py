
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for IBM (e.g., days 1001 to 1030)
start_date = '2017-01-01'  # Change to your actual start date
end_date = '2017-01-30'    # Change to your actual end date
IBM_window = IBM[start_date:end_date]

# Prepare to store correlation results
correlations = []

# Calculate rolling correlations for GE
for i in range(len(GE) - 29):  # Adjust for the 30-day window
    GE_window = GE[i:i + 30]
    corr = IBM_window.corr(GE_window)
    correlations.append(corr)

# Create a DataFrame for rolling correlations
correlation_dates = GE.index[29:]  # Dates matching the correlations
corr_df = pd.DataFrame(correlations, index=correlation_dates, columns=['Correlation'])

# Plot the correlations
plt.plot(corr_df)
plt.title('Rolling Correlation between GE and IBM (Constant IBM Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
