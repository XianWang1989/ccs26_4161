
import pandas as pd
from datetime import datetime

# Start timing
startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly with pandas
# Use the appropriate separator
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2])

# Convert the column to numeric (in case of type issues)
df[2] = pd.to_numeric(df[2], errors='coerce')

# Calculate pct_change
daily_returns = df[2].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the time taken
print(f"Time taken: {datetime.now() - startTime}")
