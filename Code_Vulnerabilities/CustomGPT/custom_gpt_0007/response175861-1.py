
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)

# Define the two stocks of interest
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the start and end dates for the fixed window of GE
start_date = '2011-01-01' # Example start date 
end_date = '2011-01-30'   # Example end date
fixed_window_GE = GE[start_date:end_date]

# Prepare a list to hold correlation values
correlation_values = []

# Loop through all possible 30-day windows in IBM
for start in range(len(IBM) - 30 + 1):
    end = start + 30
    rolling_window_IBM = IBM.iloc[start:end]
    corr = fixed_window_GE.corr(rolling_window_IBM)
    correlation_values.append(corr)

# Create a DataFrame for correlation values with the index being the dates of the rolling window
dates = IBM.index[0:len(correlation_values)]
correlation_df = pd.DataFrame(correlation_values, index=dates, columns=['Correlation'])

# Plot the correlation values
plt.plot(correlation_df)
plt.title('Rolling Correlation: GE (Fixed Window) vs. IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
