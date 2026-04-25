
import pandas as pd
from datetime import datetime

# Start time for performance tracking
start_time = datetime.now()

# Define the path to the CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file into a DataFrame
# Adjust `sep` to match your delimiter (you may use regex if needed)
df = pd.read_csv(data_path, sep='[ ;]', header=None, engine='python')

# Extract the third column (using index 2) as a column vector
ticks = df[2].astype(int)  # Convert to integers

# Calculate percentage change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Print the execution time
print("Execution time: ", datetime.now() - start_time)
