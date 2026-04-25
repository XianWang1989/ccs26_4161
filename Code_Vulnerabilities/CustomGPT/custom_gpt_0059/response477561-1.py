
import pandas as pd
from datetime import datetime

# Start timer
startTime = datetime.now()

# Define the path to your data
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify delimiters and column names
df = pd.read_csv(data_path, sep='[ ;]', header=None, engine='python')

# Extract the third column (index 2), convert to integer
ticks = df[2].astype(int)

# Create a DataFrame for ticks
deals = pd.DataFrame(ticks)

# Compute the percent change
daily_returns = deals.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print processing time
print(f"Processing time: {datetime.now() - startTime}")
