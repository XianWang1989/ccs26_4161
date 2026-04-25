
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the data path
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Load the CSV file into a DataFrame directly
# Use the correct delimiter based on your file structure
deals = pd.read_csv(data_path, delimiter=';', usecols=[2], header=None)

# Calculate the percentage change
daily_returns = deals.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

print(daily_returns)
print("Execution time:", datetime.now() - startTime)
