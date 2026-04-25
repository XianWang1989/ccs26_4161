
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly using pandas
# Adjust the separator based on your data structure
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2])

# Calculate percent change directly on the DataFrame
daily_returns = df.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - start_time)
