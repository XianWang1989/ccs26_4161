
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the correct delimiter
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2])

# Compute the percentage change
daily_returns = df.pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {datetime.now() - startTime}")
