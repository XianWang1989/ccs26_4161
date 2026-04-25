
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the file path
data_file = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Specify the delimiter and the columns to read
df = pd.read_csv(data_file, delimiter=';', usecols=[2], header=None)

# Calculate percentage change
daily_returns = df.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

print(daily_returns)
print("Time taken:", datetime.now() - start_time)
