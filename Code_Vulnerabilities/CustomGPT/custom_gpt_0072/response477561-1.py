
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Adjusting the separator to handle your specific format
data = pd.read_csv(data_path, sep='[; ]+', header=None, engine='python')

# Select the third column (index 2) and convert it to a DataFrame
ticks = data[2].astype(int)

# Calculate percentage change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - startTime)
