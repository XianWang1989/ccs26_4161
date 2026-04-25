
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to the CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file into a DataFrame
# Use the appropriate separator for your file (in this case ';')
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert to numeric (if needed)
ticks = pd.to_numeric(ticks, errors='coerce')

# Calculate percentage change
daily_returns = ticks.pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Processing time:", datetime.now() - startTime)
