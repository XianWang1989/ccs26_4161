
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window start and end
fixed_start = 1000  # For example, start from row 1001 (index 1000)
fixed_end = fixed_start + 30  # End after 30 days

# Extract the fixed window of IBM
constant_window = IBM.iloc[fixed_start:fixed_end]

# Initialize a list to hold the correlations
correlations = []

# Loop over all possible 30-day windows in GE
for start in range(len(GE) - 29):
    rolling_window = GE.iloc[start:start + 30]
    corr = constant_window.corr(rolling_window).iloc[0, 0]
    correlations.append(corr)

# Create a DataFrame for correlation results with dates
correlation_dates = GE.index[:len(correlations)]
corr_df = pd.DataFrame(correlations, index=correlation_dates, columns=['Correlation'])

# Plot the correlations
plt.plot(corr_df.index, corr_df['Correlation'])
plt.title('Correlation between IBM (Fixed) and GE (Rolling)')
plt.xlabel('Date')
plt.ylabel('Correlation Coefficient')
plt.show()
