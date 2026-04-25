
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the path to your CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV file directly using pandas
# Use appropriate delimiter and header options
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
close = df[2]

# Convert to numeric (if needed)
close = pd.to_numeric(close, errors='coerce')

# Calculate percentage change
daily_returns = close.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - start_time)
