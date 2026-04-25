
import pandas as pd
from datetime import datetime

# Start timer
startTime = datetime.now()

# Define file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Specify the delimiter as ';' to separate the columns
df = pd.read_csv(data_path, delimiter=';', engine='python', header=None)

# Extract the third column (index 2)
# Convert it to integer for calculations
df[2] = df[2].astype(int)

# Calculate the percentage change
daily_returns = df[2].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the time taken
print("Time taken:", datetime.now() - startTime)
