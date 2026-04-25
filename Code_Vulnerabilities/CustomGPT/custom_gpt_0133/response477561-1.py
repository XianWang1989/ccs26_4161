
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Reading the CSV file directly with pandas
# Use `sep` to specify your delimiters (space and semicolon)
df = pd.read_csv(data_path, sep='[ ;]', engine='python', header=None)

# Assuming the third column you want is index 2 (0-based index)
# Extract the third column to a new variable
ticks = df[2].astype(int)  # Convert directly to integer type

# Calculate the percentage change with pandas
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the daily returns to verify
print(daily_returns)

# Print the time taken
print(f"Time taken: {datetime.now() - startTime}")
