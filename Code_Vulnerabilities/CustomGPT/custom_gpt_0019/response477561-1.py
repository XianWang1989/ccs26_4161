
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file into a pandas DataFrame
# Specify the delimiter as ';' since your data seems to have both spaces and semicolons
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert the column to integers

# Calculate percentage change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', header=False)

# Print the time taken
print("Time taken:", datetime.now() - startTime)
