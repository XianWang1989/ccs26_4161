
import pandas as pd
from datetime import datetime

# Start timing
startTime = datetime.now()

# Path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the delimiter as needed
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Compute percentage change
daily_returns = ticks.pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Print elapsed time
print(f"Elapsed Time: {datetime.now() - startTime}")
