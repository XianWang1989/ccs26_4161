
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file paths
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"
output_path = r"C:\Users\eduardo\.xy\startups\returns.csv"

# Read the CSV file directly into a DataFrame
# Use `sep` to define the delimiter (considering your data format)
df = pd.read_csv(data_path, sep='[; ]', header=None, engine='python')

# Extract the third column (index 2)
ticks = df[2].astype(int)

# Calculate percentage change
daily_returns = ticks.pct_change()

# Save results to a new CSV file
daily_returns.to_csv(output_path, index=False)

print(f"Process completed in: {datetime.now() - startTime}")
