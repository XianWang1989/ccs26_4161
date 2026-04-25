
import pandas as pd
from datetime import datetime

# Measure start time
start_time = datetime.now()

# File paths
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"
output_path = "returns.csv"

# Read CSV file with appropriate delimiter
df = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2])

# Calculate percentage change
daily_returns = df.pct_change()

# Save to new CSV file
daily_returns.to_csv(output_path, index=False, header=False)

# Print execution time
print("Execution time: ", datetime.now() - start_time)
