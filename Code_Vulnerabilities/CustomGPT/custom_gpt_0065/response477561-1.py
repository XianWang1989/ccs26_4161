
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file, specifying the delimiter and relevant column
# Here, we specify that the file uses space and semicolon as delimiters
df = pd.read_csv(data_path, delimiter='[; ]', engine='python', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Calculate percentage change
daily_returns = ticks.pct_change(periods=1)

# Print the results
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Output the time taken
print("Time taken:", datetime.now() - startTime)
