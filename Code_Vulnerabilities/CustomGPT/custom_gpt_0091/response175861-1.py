
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for GE
start_date = 'your_start_date'  # e.g., '2000-01-01'
end_date = 'your_end_date'      # e.g., '2000-01-30'
GE_window = GE[start_date:end_date]

# Initialize a list to store correlation results
correlations = []

# Calculate rolling correlation
for i in range(len(IBM) - len(GE_window) + 1):
    IBM_window = IBM[i:i + len(GE_window)]
    corr = GE_window.corr(IBM_window)
    correlations.append(corr)

# Create a DataFrame for the rolling correlations with the corresponding dates
corr_dates = IBM.index[len(GE_window) - 1:]  # Align with the last date of each window
roll_cor_df = pd.DataFrame(correlations, index=corr_dates, columns=['Correlation'])

# Plot the rolling correlations
plt.plot(roll_cor_df)
plt.title('Rolling Correlation between GE and IBM')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
