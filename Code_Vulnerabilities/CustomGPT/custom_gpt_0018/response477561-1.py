
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# File paths
data = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Use pandas to read the CSV file
# Set the appropriate delimiter. If it's a combination of space and semicolon, let's specify that.
df = pd.read_csv(data, delimiter=';', header=None)  # Modify this if the structure changes

# Since you need the third column, we'll access it (which is the second index)
# Convert the column to numeric directly
df[2] = pd.to_numeric(df[2], errors='coerce')

# Calculate the percentage change
daily_returns = df[2].pct_change()

# Saving to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

print(f"Processing time: {datetime.now() - startTime}")
