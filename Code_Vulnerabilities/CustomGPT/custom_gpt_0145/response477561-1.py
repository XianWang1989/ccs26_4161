
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define CSV file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a pandas DataFrame
# Using sep argument to handle multiple delimiters; replace space and semicolon with a single delimiter
df = pd.read_csv(data_path, sep='[ ;]', engine='python', header=None)

# Extract the third column (index 2) as a DataFrame
ticks = df.iloc[:, 2]

# Convert the ticks to integer type
ticks = ticks.astype(int)

# Calculate the percentage change
daily_returns = ticks.pct_change(periods=1)

# Save the daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print(f"Time taken: {datetime.now() - startTime}")
