
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Adjust the path to where your CSV file is located
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Use pandas to read the CSV directly, specifying the delimiter
df = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2])

# Convert the third column to numeric, handling any errors
df[2] = pd.to_numeric(df[2], errors='coerce')

# Calculate percentage change
daily_returns = df.pct_change()

# Save to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {datetime.now() - startTime}")
