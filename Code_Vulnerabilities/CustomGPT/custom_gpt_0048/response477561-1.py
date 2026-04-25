
import pandas as pd
from datetime import datetime

# Start the timer
startTime = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file
# Specify the delimiter (in your case, it seems to be ';')
data = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = data[2]

# Convert the ticks to integers
ticks = ticks.astype(int)

# Create a DataFrame
deals = pd.DataFrame(ticks)

# Compute the percentage change
daily_returns = deals.pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Print the time taken
print("Time taken:", datetime.now() - startTime)
