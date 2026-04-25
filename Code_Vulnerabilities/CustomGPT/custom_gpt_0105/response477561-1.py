
import pandas as pd
from datetime import datetime

# Start timing
startTime = datetime.now()

# Define file path
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV file directly using pandas
# Specify the delimiter as necessary. Here we assume semicolon is used to separate fields.
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2, since indexing starts at 0)
ticks = df[2]

# Convert to numeric (if necessary)
ticks = pd.to_numeric(ticks, errors='coerce')

# Create DataFrame for calculations
deals = pd.DataFrame(ticks)

# Calculate percentage change
daily_returns = deals.pct_change(periods=1)

# Save to new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print elapsed time
print("Elapsed Time:", datetime.now() - startTime)
