
import pandas as pd
from datetime import datetime

# Start time for execution tracking
start_time = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Use appropriate delimiters in the read_csv function
df = pd.read_csv(data_path, sep='[; ]', engine='python', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Calculate pct_change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Print execution time
print(f"Execution time: {datetime.now() - start_time}")
