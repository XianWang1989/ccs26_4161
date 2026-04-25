
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV with pandas, specifying the delimiter
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (indexing starts at 0)
ticks = df[2]

# Convert the ticks to integers (if necessary)
ticks = ticks.astype(int)

# Compute the percentage change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the elapsed time
print(f"Processing time: {datetime.now() - startTime}")
