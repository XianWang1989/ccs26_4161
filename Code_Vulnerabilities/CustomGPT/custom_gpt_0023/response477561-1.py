
import pandas as pd
from datetime import datetime

# Start timer
startTime = datetime.now()

# File path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read CSV file with proper delimiter
# Specify both the delimiter and the column names
df = pd.read_csv(data_path, delimiter=';', header=None, names=['datetime', 'other', 'last_tick'])

# Calculate percentage change
df['pct_change'] = df['last_tick'].pct_change()

# Print the resulting DataFrame
print(df['pct_change'])

# Save to new CSV file
df[['pct_change']].to_csv('returns.csv', index=False)

# Print elapsed time
print("Elapsed time:", datetime.now() - startTime)
