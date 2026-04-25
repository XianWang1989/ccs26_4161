
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV directly into a DataFrame
# You can specify the delimiter as needed, here I assume ';' is the main delimiter
deals = pd.read_csv(data, sep=';', header=None, usecols=[2])

# Convert the third column to integers (if they are originally strings)
deals[2] = deals[2].astype(int)

# Calculate the percentage change
daily_returns = deals[2].pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print(datetime.now() - startTime)
