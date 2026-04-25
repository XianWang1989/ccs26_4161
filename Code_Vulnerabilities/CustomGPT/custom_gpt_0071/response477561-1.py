
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define file path
data_file = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV directly into a DataFrame
# Use the right delimiter (semicolon in your case) and set the appropriate header
df = pd.read_csv(data_file, delimiter=';', header=None)

# Extract the third column (index 2) and convert it to numeric
df[2] = pd.to_numeric(df[2], errors='coerce')

# Compute percentage change
daily_returns = df[2].pct_change(periods=1)

# Save the results to a new CSV
daily_returns.to_csv('returns.csv', index=False)

# Calculate execution time
print("Execution Time:", datetime.now() - start_time)
