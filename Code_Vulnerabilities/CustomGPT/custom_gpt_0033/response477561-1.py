
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Specify the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file into a DataFrame
# Use the proper delimiter in pandas
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2) and convert it to numeric
df[2] = pd.to_numeric(df[2], errors='coerce')

# Compute the percentage change
daily_returns = df[2].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {datetime.now() - start_time}")
