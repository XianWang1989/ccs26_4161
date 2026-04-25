
# Load stock prices
Stocks = pd.read_csv('StockPrices.csv', parse_dates=True, index_col=0)
IBM = Stocks['IBM']
GE = Stocks['GE']

# Define the fixed window for IBM
ibm_window_start = 1000  # index 1000 represents the starting day
ibm_window_end = 1030    # index 1030 represents the ending day
ibm_window = IBM.iloc[ibm_window_start:ibm_window_end]

# Prepare to store correlations
correlations = []

# Calculate rolling correlation for GE with the fixed IBM window
for start in range(len(GE) - 30 + 1):
    end = start + 30
    ge_window = GE.iloc[start:end]
    corr = ibm_window.corr(ge_window)
    correlations.append(corr)

# Convert the list to a DataFrame for better handling
correlation_series = pd.Series(correlations, index=GE.index[30:])

# Plot the correlations
plt.plot(correlation_series)
plt.title('Rolling Correlation between GE and Fixed IBM Window')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.show()
