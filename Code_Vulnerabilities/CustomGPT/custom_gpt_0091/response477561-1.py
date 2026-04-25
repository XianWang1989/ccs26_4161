
import pandas as pd
from datetime import datetime

# Start timer
start_time = datetime.now()

# Define the path to the CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV using pandas
data = pd.read_csv(data_path, sep=';', header=None, engine='python')

# Extract the third column (index 2)
ticks = data[2].astype(int)

# Compute percentage change
daily_returns = ticks.pct_change(periods=1)

# Save results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Print time taken
print(f"Time taken: {datetime.now() - start_time}")
