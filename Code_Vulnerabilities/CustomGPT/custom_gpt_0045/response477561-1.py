
import pandas as pd
from datetime import datetime

# Start timing
startTime = datetime.now()

# Path to the CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV file with proper separators
# Here we use 'delimiter' parameter to specify that we have mixed delimiters
df = pd.read_csv(data_path, sep='[ ;]+', header=None, engine='python')

# Extract the third column (index 2)
ticks = df[2]

# Compute the percentage change
daily_returns = ticks.pct_change(periods=1)

# Optionally, print the daily returns
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print elapsed time
print("Elapsed Time: ", datetime.now() - startTime)
