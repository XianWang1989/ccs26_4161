
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Specify your CSV file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Use the correct delimiter and skip if necessary
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)

# Calculate the percent change
daily_returns = ticks.pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print execution time
print(datetime.now() - startTime)
