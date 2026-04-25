
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV into a DataFrame
# Specify the separator as per your CSV format
df = pd.read_csv(data_path, sep=';', usecols=[2], header=None, names=["Tick"])

# Calculate percentage change
daily_returns = df['Tick'].pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - startTime)
