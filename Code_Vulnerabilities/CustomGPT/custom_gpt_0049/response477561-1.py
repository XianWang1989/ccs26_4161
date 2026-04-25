
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Load the CSV using pandas which can handle large files more efficiently
# Specify the separator based on your CSV format
df = pd.read_csv(data_path, sep='[; ]', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert to integer

# Calculate percentage change
daily_returns = ticks.pct_change(periods=1)

# Output to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - start_time)
