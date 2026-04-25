
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to the CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
deals = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2])

# Calculate the percent change
daily_returns = deals.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

print(daily_returns)
print("Execution Time:", datetime.now() - startTime)
