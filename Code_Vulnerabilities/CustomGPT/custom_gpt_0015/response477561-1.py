
import pandas as pd
from datetime import datetime

# Start timer
startTime = datetime.now()

# File path (ensure to escape backslashes or use raw string)
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file
# Using 'sep' to specify the delimiter
data = pd.read_csv(data_path, sep='[; ]+', header=None)

# Extract the third column (index 2) and convert to numeric
ticks = pd.to_numeric(data[2], errors='coerce')

# Create a DataFrame for ticks
deals = pd.DataFrame(ticks)

# Calculate percentage change
daily_returns = deals.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print processing time
print("Processing time:", datetime.now() - startTime)
