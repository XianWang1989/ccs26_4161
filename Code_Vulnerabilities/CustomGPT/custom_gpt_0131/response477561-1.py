
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to the CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file
# Specify delimiters as needed; this example assumes semicolon.
df = pd.read_csv(data_path, sep=';', usecols=[2], header=None)

# Convert the column to floats (or int if appropriate)
df[2] = df[2].astype(float)

# Calculate percentage change
daily_returns = df.pct_change()

# Save to CSV
daily_returns.to_csv('returns.csv', index=False, header=False)

print("Processing time:", datetime.now() - startTime)
