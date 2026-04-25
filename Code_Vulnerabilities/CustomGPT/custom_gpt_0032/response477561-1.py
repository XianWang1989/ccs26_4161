
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Specify the path to your CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV file, specifying the correct delimiter
# Since your data seems to use a semicolon as a delimiter, we'll use that
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert the column to numeric values (if they're not already)
ticks = pd.to_numeric(ticks)

# Calculate the percentage change
daily_returns = ticks.pct_change(periods=1)

# Save to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {datetime.now() - startTime}")
