
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# File path
data_file = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the CSV with specified delimiter
df = pd.read_csv(data_file, sep=';', header=None, usecols=[2])  # Read only the 3rd column

# Rename the column for better readability
df.columns = ['ticks']

# Calculate percentage change
daily_returns = df.pct_change()

# Save results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print time taken
print("Time taken:", datetime.now() - startTime)
