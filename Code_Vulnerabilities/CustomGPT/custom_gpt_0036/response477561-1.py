
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Use the appropriate delimiter. Here it looks like the delimiter is ';' after the first column.
# We can specify header=None because your CSV does not seem to have headers based on your format.
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2 in 0-based indexing)
# Convert the third column to numeric, errors='coerce' will replace non-convertible values with NaN
df['ticks'] = pd.to_numeric(df[2], errors='coerce')

# Calculate the percentage change
daily_returns = df['ticks'].pct_change()

# Print the daily returns
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Time taken for the operation
print(f'Time taken: {datetime.now() - startTime}')
