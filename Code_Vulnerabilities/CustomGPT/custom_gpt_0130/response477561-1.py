
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the delimiter (using ';' based on your example)
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df.iloc[:, 2]

# Convert to integers (if necessary)
ticks = ticks.astype(int)

# Create a DataFrame from the ticks
deals = pd.DataFrame(ticks)

# Calculate the percentage change
daily_returns = deals.pct_change(periods=1)

# Save the results to a new CSV
daily_returns.to_csv('returns.csv', index=False)

# Print the time taken
print("Time taken:", datetime.now() - startTime)
