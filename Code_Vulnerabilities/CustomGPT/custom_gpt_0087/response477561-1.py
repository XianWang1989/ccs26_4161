
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to the CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using Pandas
# Use the correct delimiter and specify columns to load only the necessary one
df = pd.read_csv(data_path, delimiter=';', usecols=[2], header=None)

# Rename the column for clarity
df.columns = ['Ticks']

# Calculate the percentage change
daily_returns = df['Ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print processing time
print("Processing time:", datetime.now() - startTime)
