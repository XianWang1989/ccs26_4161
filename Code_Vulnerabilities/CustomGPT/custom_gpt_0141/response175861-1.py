
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Select the two stocks
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the specific window for GE (days 1001 to 1030)
start_date = '1001'  # Adjust according to your date index in the DataFrame
end_date = '1030'
constant_GE_window = GE[start_date:end_date]

# Create an empty DataFrame to store correlations
correlations = []

# Loop over the IBM stock to calculate the correlation with the constant GE window
for i in range(len(IBM) - 30 + 1):
    # Define the current 30-day window for IBM
    current_window = IBM[i:i + 30]

    # Calculate the correlation and store it
    corr = np.corrcoef(current_window, constant_GE_window)[0, 1]
    correlations.append(corr)

# Create an index for the correlations (the dates corresponding to the starting of each window)
correlation_dates = IBM.index[:len(correlations)]

# Create a DataFrame to hold the results
corr_df = pd.DataFrame(correlations, index=correlation_dates, columns=['Correlation'])

# Plot the correlations
plt.plot(corr_df)
plt.title('Rolling Correlation between IBM and GE (Constant Window)')
plt.xlabel('Date')
plt.ylabel('Correlation Coefficient')
plt.grid()
plt.show()
