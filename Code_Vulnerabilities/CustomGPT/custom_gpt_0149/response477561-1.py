
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the delimiter as ';' and use 'sep' to handle both delimiters (space and semicolon)
df = pd.read_csv(data_path, sep='[ ;]+', header=None)

# Extract the third column (index 2) for ticks
ticks = df[2]

# Convert ticks to numeric (if not already), handling errors
ticks = pd.to_numeric(ticks, errors='coerce')

# Compute percentage change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the time taken
print("Time taken:", datetime.now() - start_time)
