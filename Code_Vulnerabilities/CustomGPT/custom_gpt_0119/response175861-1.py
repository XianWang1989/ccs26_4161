
import pandas as pd
import matplotlib.pyplot as plt

# Load stock data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define constants
window_size = 30
constant_start = 1000  # Starting index for IBM (modify as needed)

# Extract the constant window for IBM
constant_ibm_window = IBM[constant_start:constant_start + window_size]

# Initialize a list to hold correlation values
correlation_values = []

# Loop over possible windows in GE
for start in range(len(GE) - window_size + 1):
    # Get the rolling window for GE
    ge_window = GE[start:start + window_size]

    # Calculate the correlation
    correlation = constant_ibm_window.corr(ge_window)
    correlation_values.append(correlation)

# Create a DataFrame for correlation values with corresponding dates
correlation_df = pd.DataFrame(correlation_values, index=GE.index[:len(correlation_values)], columns=['Correlation'])

# Plot the correlation
plt.plot(correlation_df)
plt.title('Correlation between GE and Constant IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
