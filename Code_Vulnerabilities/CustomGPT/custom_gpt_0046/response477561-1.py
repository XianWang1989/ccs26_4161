
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Use appropriate delimiter; here it seems to be a combination of space and semicolon
data = pd.read_csv(data_path, sep='[ ;]', engine='python', header=None)

# Extract the third column (index 2)
ticks = data[2]

# Convert to DataFrame
deals = pd.DataFrame(ticks)

# Calculate percentage change
daily_returns = deals.pct_change(periods=1)

# Output the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print elapsed time
print("Elapsed time:", datetime.now() - start_time)
