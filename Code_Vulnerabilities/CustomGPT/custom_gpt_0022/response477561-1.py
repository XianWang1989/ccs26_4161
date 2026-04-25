
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Use the correct delimiter, assuming ';' is the primary separator
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert to float if necessary, and compute pct_change
daily_returns = ticks.astype(float).pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {datetime.now() - startTime}")
