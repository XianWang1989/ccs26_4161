
import pandas as pd
import matplotlib.pyplot as plt

# Load stock data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the constant window for IBM
ibm_window = 30
ibm_start = 1000  # Adjust this according to your DataFrame's index
ibm_end = ibm_start + ibm_window

# Initialize a list to store correlations
correlations = []

# Loop through GE data to get all 30-day windows
for start in range(len(GE) - ibm_window + 1):
    ge_window = GE[start:start + ibm_window]
    ibm_window_data = IBM[ibm_start:ibm_end]
    corr = ibm_window_data.corr(ge_window)
    correlations.append(corr)

# Create a DataFrame for the correlations with corresponding dates
corr_dates = GE.index[:len(correlations)]
rolling_cor = pd.Series(correlations, index=corr_dates)

# Plot the correlations
plt.plot(rolling_cor)
plt.title('Correlation between GE and IBM (Constant Window)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
