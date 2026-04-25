
import pandas as pd
from datetime import datetime

# Start time tracking
startTime = datetime.now()

# Define the path to the CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the CSV file directly into a DataFrame
# Specify the delimiter as needed (';' in your case)
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Compute the percentage change
daily_returns = ticks.pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the time taken
print(f'Time taken: {datetime.now() - startTime}')
