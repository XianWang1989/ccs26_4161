
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the delimiter and parse column names as needed
# Use `sep` to define how to split columns; here we consider both space and semicolon
df = pd.read_csv(data_path, sep='[ ;]', header=None)

# Extract the third column (index 2) into a list and convert to numeric
# This also handles any non-numeric values gracefully
ticks = pd.to_numeric(df[2], errors='coerce')

# Create a new DataFrame for the ticks
deals = pd.DataFrame(ticks)

# Calculate percentage change
daily_returns = deals.pct_change(periods=1)

# Save returns to CSV
daily_returns.to_csv('returns.csv', index=False)

# Print execution time
print(datetime.now() - startTime)
